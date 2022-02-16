#!/usr/bin/env python3

from pydoc import doc
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

app = Flask(__name__)

ARTICLES_FILENAME = "fiwiki-20181001-corpus.truncated.txt"


def get_article_dicts():
    article_dicts = []
    try:
        with open(ARTICLES_FILENAME) as file:
            soup = bs(file, 'html.parser')
        for article in soup.find_all('article'):
            article_dicts.append({'name':article['name'], 'content':article.get_text(strip=True)})
    except:
        pass
    return article_dicts


@app.route("/")
def search():
    document_dicts = get_article_dicts()
    if document_dicts:
        documents = [d['content'] for d in document_dicts if 'content' in d]
        tv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
        t_matrix = tv.fit_transform(documents).T.tocsr()
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
        return render_template('index.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
