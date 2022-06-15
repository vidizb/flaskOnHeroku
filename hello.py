from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
   from flask import Flask, render_template

@app.route("/works")
def it_works():
    return "siap bapak"
