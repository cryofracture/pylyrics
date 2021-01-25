from flask import Flask, render_template, flash, redirect, request
from flask_bootstrap import Bootstrap
import psycopg2
from dotenv import load_dotenv
import os
import requests
from flask_nav import Nav
from flask_nav.elements import *
load_dotenv()

nav = Nav()
app = Flask(__name__)
Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

@nav.navigation()
def mynavbar():
    return Navbar('PyLyrics', View('Home', 'Random'),)

nav.init_app(app)

@app.route('/', methods=['GET'])
def index():
    title = "PyLyrics Home"
    return render_template('index.html', title=title, active=True)

@app.route('/results', methods=['POST'])
def results():
    title = "PyLyrics Results"
    artist = request.form.get('artistName')
    song = request.form.get('songName')
    artist = artist.replace(" ","-")
    song = song.replace(" ", "-")
    song = song.capitalize()
    response = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
    lyric_load = response.json()
    song = song.replace("-", " ")
    artist = artist.replace("-", " ")
    lyrics = lyric_load['lyrics']

    return render_template('results.html', song=song, artist=artist, lyrics=lyrics, title=title)


if __name__ == '__main__':
    app.run(debug=True)



"""
<!-- <a class="nav-item nav-link {% if active %} active {% endif %}" href="{{url_for('random')}}">Get Lyrics to a random song<span class="sr-only"></span></a> -->
"""