import flask
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello World</h1>"



app.run()