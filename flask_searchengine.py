#!/usr/bin/env python3

from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

ARTICLES_FILE = "data/enwiki-20181001-corpus.1000-articles.txt"

app = Flask(__name__)


document_dicts = []
with open(ARTICLES_FILE) as file:
    soup = bs(file, 'lxml')
for article in soup.find_all('article'):
    document_dicts.append({'name':article['name'], 'content':article.get_text(strip=True)})
documents = [d['content'] for d in document_dicts if 'content' in d]
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
                matches.append({'hit':"{:d}".format(i+1), 'score':"{:.4f}".format(score), 'name':"{:s}".format(document_dicts[id]['name']), 'content':"{:.100s}…".format(document_dicts[id]['content'])})
        except:
            pass
    return render_template('index.html', matches = matches)


if __name__ == '__main__':
    app.run(debug = False)
