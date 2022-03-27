#!/usr/bin/env python3


from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')


from app.functionality.indexing import index
from app.functionality.search import search
from app.functionality.visualisation import visualise
from sklearn.feature_extraction.text import TfidfVectorizer


VECTORIZER = TfidfVectorizer(lowercase = True, sublinear_tf = True, use_idf = True, norm = "l2")
DATA = "app/data/data.json"


data_dictionaries, data_matrix = index(VECTORIZER, DATA)


@app.route('/')
def main():
    query = request.args.get('query')
    matches = []
    if query:
        try:
            matches = search(VECTORIZER, data_dictionaries, data_matrix, query)
            #visualise(matches)
        except:
            pass
    return render_template('index.html', matches = matches)
