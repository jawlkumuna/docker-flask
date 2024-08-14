"""Main webapp module"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/morning")
def morning():
    return "Good morning!"
