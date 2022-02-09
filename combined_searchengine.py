#!/usr/bin/env python3

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup as bs
import numpy as np


D = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}

ARTICLES_FILENAME = "fiwiki-20181001-corpus.truncated.txt"


def get_engine():
    print()
    while True:
        user_input = input("Please type ‘b’ to use Boolean search or ‘t’ to use TF-IDF cosine-similarity search: ").strip()
        if user_input == "b":
            print("Using Boolean search…")
            return "b"
        elif user_input == "t":
            print("Using TF-IDF cosine-similarity search…")
            return "t"


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


def rewrite_token(t):
    return D.get(t, 'sparse_td_matrix[cv.vocabulary_["{:s}"]].todense()'.format(t))


def rewrite_query(query):
    return " ".join(rewrite_token(t) for t in query.split())


def boolean_search(query):
    hits_matrix = eval(rewrite_query(query))
    hits_list = list(hits_matrix.nonzero()[1])
    print()
    print("Your query ‘{:s}’ matches the following documents:".format(query))
    for i, doc_id in enumerate(hits_list):
        print("Hit #{:d}: {:.100s}".format(i, documents[doc_id]))


def tfidf_cosine_search(query):
    query_vector = tv.transform([query]).tocsc()
    hits = np.dot(query_vector, t_matrix)
    ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse=True)
    print()
    print("Your query ‘{:s}’ matches the following documents:".format(query))
    for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
        print("Hit #{:d} (score: {:.4f}): {:.100s}".format(i, score, documents[id]))


if __name__ == '__main__':
    documents = get_articles()
    cv = CountVectorizer(lowercase=True, binary=True, token_pattern=r'(?u)\b\w\w*\b')
    c_matrix = cv.cv.fit_transform(documents).T.tocsr()
    tv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
    t_matrix = tv.fit_transform(documents).T.tocsr()
    engine = get_engine()
    while True:
        try:
            query = get_query()
            if query:
                if engine == "b":
                    boolean_search(query)
                elif engine == "t":
                    tfidf_cosine_search(query)
            else:
                break
        except KeyError:
            print("Your query produced no results, please try another query.")
