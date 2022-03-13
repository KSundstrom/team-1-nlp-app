#!/usr/bin/env python3

from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import datacollection

ARTICLES_FILE = "data/enwiki-20181001-corpus.1000-articles.txt"

app = Flask(__name__)




documents = [d['place'] for d in datacollection.entries_json if 'place' in d]
tv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
t_matrix = tv.fit_transform(documents).T.tocsr()


@app.route('/')
def search():
    query = request.args.get('query')
    matches = []
    if query:
        try:
            query_vector = tv.transform([query]).tocsc()
            hits = np.dot(query_vector, t_matrix)
            ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse=True)
            for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
                matches.append({'hit':"{:d}".format(i+1), 'score':"{:.4f}".format(score), 'place':"{:s}".format(datacollection.entries_json[id]['place']), 'forecast/warning':"{:.100s}…".format(datacollection.entries_json[id]['forecast'])})
        except:
            pass
    return render_template('index.html', matches = matches)


if __name__ == '__main__':
    app.run(debug = False)
