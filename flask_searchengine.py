#!/usr/bin/env python3

from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

ARTICLES_FILENAME = "fiwiki-20181001-corpus.truncated.txt"


def get_article_dicts():
    try:
        with open(ARTICLES_FILENAME) as file:
            soup = bs(file, 'html.parser')
        article_dicts = []
        for article in soup.find_all('article'):
            article_dicts.append({"name":article['name'], "content":article.get_text(strip=True)})
        return article_dicts
    except OSError:
        return None


@app.route("/")
def search():
    document_dicts = get_article_dicts()
    query = request.args.get('query')
    matches = []
    if query:
        for d in document_dicts:
            if query.lower() in d['content'].lower():
                matches.append(d)
    return render_template('index.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)
