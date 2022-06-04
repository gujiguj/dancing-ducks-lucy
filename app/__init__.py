import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

fellows = {
    'lucy': {
        "first": "Lucy",
        "last": "Wang",
        "github": "https://github.com/gujiguj",
        "linkedin": "https://www.linkedin.com/in/lucy-wang-a73267191/",
        "resume": "",
        "about": "Hello! I am Lucy Wang. I'm majoring in Computer Science and minoring in Japanese at Villanova University.",
        "image": "",
        "education": {
            0: {
                "institution": "Villanova University",
                "grad_date": "May 2023",
                "courses": "Computer Science",
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
        "github": "https://github.com/yanbmia",
        "linkedin": "https://www.linkedin.com/in/yanbmia/",
        "resume": "",
        "about": "Hey, I'm Mia Yan. I'm a incoming sophmore at Binghamton University studying computer science.",
        "image": "",
        "education": {
            0: {
                "institution": "Binghamton University",
                "grad_date": "May 2025",
                "courses": "Computer Science",
            }
        },
        "experience": {
            0: {
                "position": "Operations Intern",
                "company": "Xenon Health, Inc.",
                "dates": "July 2021 - November 2021",
                "desc": " blah blah ",
            }
        },
        "hobbies": {
            
        }
    },
    'rodrigo': {
        "first": "Rodrigo",
        "last": "",
        "github": "",
        "linkedin": "",
        "resume": "",
        "about": "",
        "image": "",
        "education": {
            0: {
                "institution": "",
                "grad_date": "",
                "courses": ""
            }
        },
        "experience": {
            0: {
                "position": "",
                "company": "",
                "dates": "",
                "desc": "",
            }
        },
        "hobbies": {
            0: {
                "name": "",
                "image": "",
                "desc": ""
            },
            1: {
                "name": "",
                "image": "",
                "desc": "",
            },
            2: {
                "name": "",
                "image": "",
                "desc": ""
            }
        }
    },
    'kelly': {
        "first": "Kelly",
        "last": "",
        "github": "",
        "linkedin": "",
        "resume": "",
        "about": "",
        "image": "",
        "education": {
            0: {
                "institution": "",
                "grad_date": "",
                "courses": ""
            }
        },
        "experience": {
            0: {
                "position": "",
                "company": "",
                "dates": "",
                "desc": "",
            }
        },
        "hobbies": {
            0: {
                "name": "",
                "image": "",
                "desc": ""
            },
            1: {
                "name": "",
                "image": "",
                "desc": "",
            },
            2: {
                "name": "",
                "image": "",
                "desc": ""
            }
        }
    },
}

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/fellow/<name>')
def show_profile(name):
    return render_template('profile.html', title=fellows[name]['first']+' '+fellows[name]['last'], fellow=fellows[name], url=os.getenv("URL"))

