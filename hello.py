from flask import Flask, render_template
from models import HelloModel

app = Flask(__name__)

@app.route("/")
def index():
   model = HelloModel()
   
   # mengirim model ke view
   return render_template('hello.html', model=model)

@app.route("/works")
def it_works():
    return "siap bapak"
