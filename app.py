from cgitb import text
from flask import Flask, request, render_template
from stories import story

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "project"
debug = DebugToolbarExtension(app)

@app.route('/home')
def home_page():
    # hold the story prompts
    prompts = story.prompts
    # pass the story prompts to our template in home.html
    return render_template("home.html", prompts=prompts)

@app.route('/story')
def story_page():
    # generates story with args gathered from input form on /home
    text = story.generate(request.args)
    # pass the story text to story.html
    return render_template("story.html", text=text)