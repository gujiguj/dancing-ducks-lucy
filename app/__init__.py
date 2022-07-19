import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re

# dictionary of all information about fellows. Will be passed in a render_template call and used in a jinja template.
fellows = {
    "lucy": {
        "first": "Lucy",
        "last": "Wang",
        "github": "https://github.com/gujiguj",
        "linkedin": "https://www.linkedin.com/in/lucy-wang-a73267191/",
        "resume": "",
        "about": "Hi, I'm Lucy Wang! I'm from Newark, DE, and I'm studying Computer Science and Japanese at Villanova University. I like learning things that pique my interest! I also like cats, snoozing, and drawing cute things.",
        "image": "/static/img/lucy-mlh.jpeg",
        "education": [
            {
                "institution": "Villanova University",
                "grad_date": "May 2023",
                "major": "B.S. Computer Science",
                "courses": "Algorithms & Data Structures, Analysis of Algorithms, Discrete Structures, Theory of Computation, Organization of Programming Languages, Linear Algebra for Computing, Computer Systems, Principles of Database Systems, Platform-based Computing, Software Engineering, Computer Ethics, Computer Graphics"
            }
        ],
        "experience": [
            {
                "position": "IT Assistant",
                "company": "Sepax Technologies, Inc.",
                "dates": "July 2020 - August 2020, May 2022 - present",
                "desc": "Maintained network of office computers, printers, and cameras, company intranet, and company's external marketing website. Used HTML/CSS, PHP, and MySQL to update and add features to the intranet and external website. Carried out general help desk tasks (e.g. setting up new desktops, assigning emails, troubleshooting network issues, and monitoring network security).",
                "image": "/static/img/sepax.png"
            }
        ],
        "hobbies": [
            {
                "name": "Art",
                "image": "/static/img/artwork.png",
                "desc": "I've been drawing in an anime/manga style since I was very young. I like drawing cute designs and designs that I find beautiful. While I often find myself unable to think of what to draw, I become super driven when I'm drawing for other people. Nothing makes me happier than creating for others!"
            },
            {
                "name": "Gaming",
                "image": "/static/img/genshin.jpg",
                "desc": "I'm a casual gamer. I only own a Macbook so I can't play a lot of games, so I just dabble in some mobile games! I mainly play an RPG called Genshin Impact, but I also play some of a tower defense game called Arknights. As for computer games, I'm currently playing the indie platformer Celeste! I've also casually played Minecraft, Terraria, and Portal.",
            },
            {
                "name": "Anime & Manga",
                "image": "/static/img/chronocrusade.jpg",
                "desc": "I love reading manga! And I also enjoy watching anime, but since it takes more time I don't do it as often :( My favorite manga is Chrono Crusade! I also love Witch Hat Atelier and Frieren at the Funeral. And my favorite anime is... it's so hard to choose! Maybe Ouran High School Host Club..."
            }
        ],
        "locations": [
            {
                "location": "China",
                "coordinates": [31.224361, 121.469170],
                "desc": "I visited my relatives in China when I was very young. I went to Shanghai, Xiangtan in Hunan province, and the countryside in Henan province. I don't remember much, but if you're visiting the countryside, definitely be prepared for the mosquitoes!"
            },
            {
                "location": "Taiwan",
                "coordinates": [22.999727, 120.227028],
                "desc": "I taught English to elementary and middle school students in various schools in Tainan, Taiwan for two weeks. I know Mandarin Chinese, but it was hard even when I had a teaching partner! At one school, we did not have enough people on our team and I had to teach solo! Still, it was a very exciting experience. Taiwan is a great place to visit!"
            },
            {
                "location": "Alaska",
                "coordinates": [63.129887, -151.197418],
                "desc": "I traveled to Alaska with family! The highlight of our trip was visiting Denali National Park, where we got to see Mt. Denali, moose, caribou, bears, and even a few wolves (in the distance). Alaska is full of preserved nature, which is evidenced by the fact bugs still get smashed against car windshields there!"
            },
            {
                "location": "Las Vegas, NV",
                "coordinates": [36.114647, -115.172813],
                "desc": "I visited Las Vegas but... before I was 18! So I couldn't touch any of the casinos... Las Vegas is a very shiny place with some good food! I recommend visiting Serendipity for iced hot chocolate."
            },
            {
                "location": "Yellowstone National Park",
                "coordinates": [44.423691, -110.588516],
                "desc": "Yellowstone National Park is very cool. The whole park has so many thermal pools that are the most beautiful shade of blue. Our tour guide actually lost his hat in one of the pools (he did not get it back)!"
            }
        ]
    }
}

load_dotenv()
app = Flask(__name__)

# Implemented TESTING mode that allows for interacting with an in-memory test database

testing = True if os.getenv("TESTING") == "true" else False
if testing:
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri = True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )
    # if not testing: mydb.close()

# creates a class to define a table for Peewee
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    # date
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

print(mydb)
if not testing: mydb.close() 

# home page / about
# input the dictionary of information
@app.route('/')
def show_profile(name="lucy"):
    return render_template('profile.html', title=fellows[name]['first']+' '+fellows[name]['last'], fellow=fellows[name], url=os.getenv("URL"))

@app.route('/hobbies')
def show_hobby():
    return render_template('hobbies.html', title="Hobbies", fellows=fellows, url=os.getenv("URL"))

@app.route('/map')
def show_map():
    return render_template('map.html', title="Travel", fellows=fellows, url=os.getenv("URL"))

# adds a timeline post to the db via POST method
# the date in the instance is just the current date/time
@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    # Added try-except blocks for catching improper inputs attempting to be used in a post, such as missing or improper values.
    try:
        name = request.form['name']
    except:
        return "Invalid name (missing)", 400
    if name == "":
        return "Invalid name (improper value)", 400
    try:
        email = request.form['email']
    except:
        return "Invalid email (missing)", 400

    if not re.fullmatch("^([A-Za-z\d\.\-_]+)@([A-Za-z\d\-_]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$", email):
        return "Invalid email (improper value)", 400

    try:
        content = request.form['content']
    except:
        return "Invalid content (missing)", 400

    if request.form.get('content', "") == "":
        return "Invalid content (empty)", 400

    # calls TimelinePost class to create a new instance
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    if not testing: mydb.close()

    return model_to_dict(timeline_post)

# retrives all timeline posts, ordered by created_at (creation time) descending
# returns a dictionary
@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    posts = [ model_to_dict(p) for p in TimelinePost.select().order_by(TimelinePost.created_at.desc()) ]
    # timeline_posts = [ model_to_dict(p) for p in posts ]
    if not testing: mydb.close()
    return {
        'timeline_posts': posts
    }

@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_timeline_post(id):
    post_to_delete = TimelinePost.get(TimelinePost.id == id)
    deleted_post = model_to_dict(post_to_delete)
    post_to_delete.delete_instance()
    if not testing: mydb.close()

    return deleted_post

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title='Timeline', timeline=get_timeline_post())
