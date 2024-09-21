# flask app
from flask import Flask

flaskapp = Flask(__name__)

@flaskapp.route("/")
def hello():
    return "<p>Hello, globe!<p>"