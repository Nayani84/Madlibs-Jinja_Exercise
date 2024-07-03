from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "abcdef"

debug = DebugToolbarExtension(app)


@app.route("/")
def question_form():
    """Generate form prompting for all the words in the story"""
    
    prompts = story.prompts
    return render_template("home.html" , prompts=prompts)


@app.route("/story")
def my_story():
    """Resulting Madlib story"""

    answers = request.args
    text = story.generate(answers)
    return render_template("story.html" , text=text)