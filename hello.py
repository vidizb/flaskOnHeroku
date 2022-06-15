from flask import Flask
from models import HelloModel

app = Flask(__name__)

@app.route("/")
def index():   
   return render_template('hello.html')


@app.route("/works")
def it_works():
    return "siap bapak"
