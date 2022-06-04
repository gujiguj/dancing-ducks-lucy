import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

fellows = {
    'lucy': {
        "first": "Lucy",
        "last": "Wang",
        "about": "Hello! I am Lucy Wang. I'm majoring in Computer Science and minoring in Japanese at Villanova University.",
        "image": "",
        "education": {
            0: {
                "institution": "Villanova University",
                "grad_date": "May 2023",
                "courses": "Computer Science"
            },
            1: {
                "institution": "School",
                "grad_date": "date",
                "courses": "courses"
            }
        },
        "experience": {
            0: {
                "position": "IT Assistant",
                "company": "Sepax Technologies, Inc.",
                "dates": "June 2020 - July 2020, May 2022 - August 2022",
                "desc": "I helped out with IT tasks. Troubleshooted problems with office machines (printers and computers) and issues with the local network. Used MySQL, HTML/CSS, Javascript, and PHP for web development of the intranet and external website. Utilized Python to log issues with servers hosting the db, website, intranet, and camera systems.",
            }
        },
        "hobbies": {
            0: {
                "name": "Art",
                "image": "",
                "desc": "I love to draw! I mainly do sketches of characters in an anime style on my iPad. I love drawing for other people, especially if they have cool character designs!"
            },
            1: {
                "name": "Gaming",
                "image": "",
                "desc": "I'm a casual gamer. I only own a Macbook so I can't play a lot of games, so I just dabble in some mobile games! I mainly play Genshin Impact, but I also play Arknights. As for computer games, I'm currently playing Celeste! I've also casually played Minecraft, Terraria, and Portal.",
            },
            2: {
                "name": "Anime/Manga",
                "image": "anime.jpg",
                "desc": "As one might have guessed from my artistic hobby, I like watching anime and reading manga. My favorite manga is Chrono Crusade!"
            }
        }
    },
    'mia': {
        "first": "Mia",
        "last": "Yan",
        "about": "",
        "image": "",
        "education": {
            0: {
                "institution": "",
                "grad_date": ""
            }
        },
        "experience": {
            
        },
        "hobbies": {
            
        }
    }
}

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/fellow/<name>')
def show_profile(name):
    return render_template('profile.html', title=fellows[name]['first']+' '+fellows[name]['last'], fellow=fellows[name], url=os.getenv("URL"))

