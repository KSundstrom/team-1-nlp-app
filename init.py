import os
from flask import Flask
import flask_searchengine


# create and configure the app
app = Flask(__name__, instance_relative_config=True)

@app.route('/hello')
def main():
    matches = []
    flask_searchengine.search()
    return flask_searchengine.results(matches)
    

