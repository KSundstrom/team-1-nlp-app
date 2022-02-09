#!/usr/bin/env python3

from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup as bs
import numpy as np


ARTICLES_FILENAME = "fiwiki-20181001-corpus.truncated.txt"


def get_articles():
    try:
        with open(ARTICLES_FILENAME) as file:
            soup = bs(file, 'html.parser')
        articles = []
        for article in soup.find_all('article'):
            articles.append(article.get_text(strip=True))
        return articles
    except OSError:
        print("Error trying to read from file {:s}!".format(ARTICLES_FILENAME))


def get_query():
    print()
    return input("Please enter a query or press enter to exit: ").strip()


def tfidf_cosine_search(query):
    query_vector = tv.transform([query]).tocsc()
    hits = np.dot(query_vector, t_matrix)
    ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse=True)
    print()
    print("Your query '{:s}' matches the following documents:".format(query))
    for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
        print("Hit #{:d} (score: {:.4f}): {:.100s}".format(i, score, articles[id]))


if __name__ == '__main__':
    articles = get_articles()
    tv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
    t_matrix = tv.fit_transform(articles).T.tocsr()
    while True:
        try:
            query = get_query()
            if query:
                tfidf_cosine_search(query)
            else:
                break
        except KeyError:
            print("Your search provided no results, please try another query.")
