from flask import Flask
from models import HelloModel

app = Flask(__name__)

@app.route("/")
def index():
   # membuat objek dari kelas HelloModel
   model = HelloModel()
   
   # mengembalikan nilai yang diambil dari model
   return model.getText()

@app.route("/works")
def it_works():
    return "siap bapak"
