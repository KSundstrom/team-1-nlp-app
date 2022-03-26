#!/usr/bin/env python3


from flask import Flask, render_template, request


app = Flask(__name__)


from sklearn.feature_extraction.text import TfidfVectorizer
from app import app
#import data
#import indexing
#import search
#import visualisation


VECTORIZER = TfidfVectorizer(lowercase = True, sublinear_tf = True, use_idf = True, norm = "l2")
TEST_SOURCE_PATH = "testcorpus.txt"


#datacollection
#document_dictionaries, document_matrix = indexingengine(VECTORIZER, TEST_SOURCE_PATH)


@app.route('/')
def index():
    query = request.args.get('query')
    if query:
        try:
            pass
            #matches = searchengine(VECTORIZER, document_dictionaries, document_matrix, query)
            #visualisationengine
        except:
            pass
    return render_template('index.html', matches = matches)
