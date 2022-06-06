import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

# dictionary of all information about fellows. Will be passed in a render_template call and used in a jinja template.
# "name": {
#         "first": "",
#         "last": "",
#         "about": "",
#         "image": "",
#         "socials": [
#             {
#                 "name": "",
#                 "link": ""
#             }
#         ],
#         "education": [
#             {
#                 "institution": "",
#                 "grad_date": "",
#                 "courses": "",
#             }
#         ],
#         "experience": [
#             {
#                 "position": "",
#                 "company": "",
#                 "dates": "",
#                 "desc": ""
#             }
#         ],
#         "resume": "",
#         "hobbies": [
#             {
#                 "name": "",
#                 "image": "",
#                 "desc": ""
#             }
            
#         ]
#     }
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
                "courses": "Computer Science"
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
    },
    'mia': {
        "first": "Mia",
        "last": "Yan",
        "github": "https://github.com/yanbmia",
        "linkedin": "https://www.linkedin.com/in/yanbmia/",
        "resume": "",
        "about": "Hey, I'm Mia! I'm originally from Brooklyn, New York. I currently an undergrad student studying Computer Science. I'm a creative person. I love anything design and art-related. I've always been an indecisive person, but one thing I always knew I wanted to do is to travel the world.",
        "image": "/static/img/mia-mlh.jpg",
        "education": [
            {
                "institution": "Binghamton University",
                "grad_date": "May 2025",
                "courses": "Computer Science",
            }
        ],
        "experience": [
            {
                "position": "Operations Intern",
                "company": "Xenon Health, Inc.",
                "dates": "July 2021 - November 2021",
                "desc": "I managed several company spreadsheets, conducted crucial business research, and presented various avenues and methods to improve company outreach and communication.",
            }
        ],
        "hobbies": [
            {
                "name": "Reading",
                "image": "/static/img/reading.jpeg",
                "desc": "I'm a staunch supporter of the library--endless free books! When I was a kid I read a lot, but somewhere in middle school and high school, I grew a distaste for reading. But now I read all the time. My favorite authors are James Baldwin, Dostoevsky, and Murakami. (If you don't have a local library card, what are you doing? You must get one.)"
            },
            {
                "name": "Film",
                "image": "/static/img/film.jpeg",
                "desc": "Is watching movies a hobby? Do I need to present my letterbox account and distinguish between films and movies to prove it? I feel like I can never pick a favorite movie. But I do love all genres--sci-fi, romance, action--maybe everything except thriller.",
            },
        ],
        "locations": [
            {
                "location": "London, UK",
                "coordinates": [51.506180, -0.120142],
                "desc": "I swear summer doesn't exist in London. And yes, I will continue to call the Underground the subway."
            },
            {
                "location": "Rainham, UK",
                "coordinates": [51.366388, 0.611494],
                "desc": "My aunt and cousin moved here in 2019, so of course, I had to visit. (And by visit I totally don't mean I didn't want to pay hotel fees.)"
            },
            {
                "location": "Trinidad and Tobago",
                "coordinates": [10.170945, -61.675227],
                "desc": "My mom is from here! I've been here lots of times to see my family."
            },
            {
                "location": "Miami, FL",
                "coordinates": [25.771533, -80.192114],
                "desc": "Went here in August...I've never experienced humidity like this before."
            },
            {
                "location": "Nassau, The Bahamas",
                "coordinates": [25.044149, -77.354166],
                "desc": "The ocean here is unreal. I was on a cruise with my family when I was 12 and we stopped here."
            },
            {
                "location": "Belize",
                "coordinates": [17.507322, -88.203623],
                "desc": "My mom's uncle's wife is from here! The vibes in Belize are spectacular."
            },
            {
                "location": "Hubei, China",
                "coordinates": [30.703383, 111.292291],
                "desc": "I went only went once when I was very little to visit my dad's family. The food was very good though."
            },
            {
                "location": "Shanghai, China",
                "coordinates": [31.241374, 121.457556],
                "desc": "This city is amazing. I really want to go back soon."
            },
            {
                "location": "Montreal, Canada",
                "coordinates": [45.498696, -73.570269],
                "desc": "One morning, I went to have brunch and the waitress asked me what I wanted to order in French, guess you can say I'm a local. *sarcasm ;)"
            },
            {
                "location": "Southampton, NY",
                "coordinates": [40.884612, -72.393004],
                "desc": "Unfortunately, the Hamptons aren't overhyped. It's really fun here in the summer."
            },
            {
                "location": "Boston, MA",
                "coordinates": [42.358876, -71.056763],
                "desc": "When I was a kid, my family used to take a lot of random road trips. But I'm marking Boston down because I have some funny childhood photos here."
            },
        ]
    },
    "rodrigo": {
        "first": "Rodrigo",
        "last": "Lara",
        "github": "https://github.com/RodrigoLaraM",
        "linkedin": "https://www.linkedin.com/in/rodrigolaram/",
        "resume": "",
        "about": "Hi! I'm Rodrigo Lara. A rising senior at Michigan State University majoring in Data Science",
        "image": "/static/img/lara-mlh.jpg",
        "education": [
            {
                "institution": "Michigan State University",
                "grad_date": "December 2023",
                "courses": "Data Science"
            }
        ],
        "experience": [
            {
                "position": "Teaching Assistant",
                "company": "Michigan State University",
                "dates": "January 2022 - May 2022",
                "desc": "I taught an introductory Python programming and algorithmic thinking course to 35 students.",
            }
        ],
        "hobbies": [
            {
                "name": "Reading",
                "image": "/static/img/books.jpeg",
                "desc": "I'm mainly interested finance, geopolitics and phylosophy"
            },
            {
                "name": "Music Production",
                "image": "/static/img/ableton.png",
                "desc": "On free times I write electronic music",
            }
        ],
        "locations": [
            {
                "location": "Paris, FR",
                "coordinates": [48.8566, 2.3522],
                "desc": "Beuatiful Eiffel Tower"
            },
            {
                "location": "Barcelona, SP",
                "coordinates": [41.3874, 2.1686],
                "desc": "Best 'Jamon Serrano' I've ever had"
            },
            {
                "location": "Reynosa, MX",
                "coordinates": [26.0508, -98.2979],
                "desc": "The city I was raised in"
            },
            {
                "location": "Chicago, IL",
                "coordinates": [41.8781, -87.6298],
                "desc": "I went once to see my favorite artist, Flume, at Lollapalooza"
            },
            {
                "location": "Cancun. MX",
                "coordinates": [21.1619, -86.8515],
                "desc": "Some of the most beautiful beaches in Mexico."
            }
        ]
    },
    "kelly": {
        "first": "Kelly",
        "last": "Chen",
        "github": "https://github.com/Kelly0921",
        "linkedin": "https://www.linkedin.com/in/kellychen0921/",
        "resume": "",
        "about": "Hey! I'm Kelly from Plano, TX. I'm known as the one who's always driven to learn new skills, and I'm always looking forward to challenges to help me grow beyond my limits. I enjoy researching the latest technology trends, exploring different software, and sharing these ideas with others. I'm also passionate about entreprenurship, and I'm currently working on my own project building a unique payment gateway service. During my free time, as a woman in STEM, I’m always active in multiple Women in STEM communities, I often participate in workshops and other conferences to advocate for girls in STEM and educate potential students on their path to STEM.",
        "image": "/static/img/kelly-mlh.jpg",
        "education": [
            {
                "institution": "Lehigh University",
                "grad_date": "May 2025",
                "courses": "Computer Science and Business"
            }
        ],
        "experience": [
            {
                "position": "Managing Editor for Clubs and Organizations & Photographer",
                "company": "Epitome Yearbook",
                "dates": "Jan 2022 - Present",
                "desc": "-Communicated with clubs/organizations and campus partners for photos and copy to complete spreads. -Assigned clubs to spaces on the ladder and worked with Editor in Chief to assign associate editors to layouts. -Student liaison with the Office of Student Engagement Office. -Helped to recruit students at Club Expo.",
            },
            {
                "position": "Marketing Intern",
                "company": "rThreat",
                "dates": "Feb 2021 - Jun 2021",
                "desc": "-Implemented digital and online marketing tactics to drive new subscriber acquisitions and retain existing subscribers. -Designed social media content using prior marketing templates and customized WordPress blogs to boost search engine optimization (SEO). -Helped to reevaluate the business transformation capabilities for a unique market positioning on breach and attack emulation. -Conducted research and assembled cybersecurity resources for 7 blogs. -Gained access to CISO interviews & Breach and Attack Emulation Lab."
            },
            {
                "position": "Chief Operating Officer",
                "company": "Online Impacts",
                "dates":"Aug 2020 - May 2021",
                "desc": "-Revamped the method to oversee a group of remote volunteers through Trello and Slack. -Proposed new marketing ideas that focused on digital marketing to raise publicity and helped to get featured on 5 news platforms. -Developed a partnership contract used to grow strategic partnerships and helped to outreach to potential partners. -Counseled nonprofit organizations about their websites and presented requests to the web development team. -Engaged in the bi-weekly technological innovation meeting to brainstorm ideas and served as the meeting minute taker.",
            },
            {
                "position":"Staff (Chinese Fluency Project Leader / Coding Intern / Marketing & Communications Intern)",
                "company":"Break Diving",
                "dates":"Dec 2018 - Nov 2020",
                "desc":"-Modified the action menu design and coded additional features on the community and organization site. -Tested team member's pull requests for proper functionality, accessibility, and presentation regularly. -Designed 14 dive certificate templates used to certify 50+ dives and managed the dive certification program. -Oversaw the Chinese chatroom of 30+ members. -encouraged member participation regularly and provided assistance to members in need.",
            }
        ],
        "hobbies": [
            {
                "name": "Boardgames",
                "image": "/static/img/boardgames.png",
                "desc": "A pretty new habit for me. It's a great way to make new friends and have fun. Some of the boardgames that I play include Ticket to Ride, Rival Restaurant, Mahjong, Exploding Kittens."
            },
            {
                "name": "Sketching",
                "image": "/static/img/kelly-drawing.png",
                "desc": "I like drawing sometimes when I'm free. It helps me focus and concentrate on doing one task. ",
            },
            {
                "name": "Planning/Organizing",
                "image": "/static/img/workspace.png",
                "desc": "I find satisfaction when I plan out my day and accomplish my goals. I try my best to give myself sometimes to reflect on myself everyday, every week, every month, and every year. It helps me to focus on my goals and stay on track."
            },
            {
                "name": "Movie (Especially Crime Documentaries)",
                "image": "/static/img/kelly-film.png",
                "desc": "I enjoy watching crime documentaries and even listening to true-crime podcasts."
            }
        ],
        "locations": [
            {
                "location": "Sichuan, China",
                "coordinates": [30.6509, 104.0757],
                "desc": "I went to Sichuan at a young age and stayed there for 11 years. If you don't know it, it's the home of pandas and full of spicy hotpots!"
            },
            {
                "location": "Henan, China",
                "coordinates": [34.7657, 113.7532],
                "desc": "This is where my dad is from, so my family would go visit during the summer before we moved back to U.S."
            },
            {
                "location": "Las Vegas, United States",
                "coordinates": [36.1716, 115.1391],
                "desc": "Went during winter break, and I had a lot of fun there visiting different hotels!"
            },
            {
                "location": "Walt Disney World, United States",
                "coordinates": [28.3772, 81.5707],
                "desc": "A trip full of magic! Super fun watching the performances and meeting the characters, but the line is TOOOO long."
            },
            {
                "location": "San Antonio, United States",
                "coordinates": [29.4252, 98.4946],
                "desc": "Very beautiful place full of Texas history."
            },
        ]
    },
}

load_dotenv()
app = Flask(__name__)

# home page route
@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), fellows=fellows)

# fellow's pages route
# input the dictionary of a fellow's information using fellows[name]
@app.route('/fellow/<name>')
def show_profile(name):
    return render_template('profile.html', title=fellows[name]['first']+' '+fellows[name]['last'], fellow=fellows[name], url=os.getenv("URL"))

@app.route('/hobbies')
def show_hobby():
    return render_template('hobbies.html', title="Travel", fellows=fellows, url=os.getenv("URL"))

@app.route('/map')
def show_map():
    return render_template('map.html', title="Travel", fellows=fellows, url=os.getenv("URL"))
