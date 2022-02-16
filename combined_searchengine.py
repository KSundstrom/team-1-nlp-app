#!/usr/bin/env python

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup as bs
import numpy as np

D = {"and": "&", "or": "|", "not": "1 -", "(": "(", ")": ")"}

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


def get_article_dicts():
    try:
        with open(ARTICLES_FILENAME) as file:
            soup = bs(file, 'html.parser')
        article_dicts = []
        for article in soup.find_all('article'):
            article_dicts.append({"name":article['name'], "content":article.get_text(strip=True)})
        return article_dicts
    except OSError:
        print("Error trying to read from file {:s}!".format(ARTICLES_FILENAME))


def get_lowercase_query():
    print()
    raw = input("Please enter a query or press enter to exit: ")
    stripped = raw.strip()
    lowercased = stripped.lower()
    return lowercased


def rewrite_token(token):
    return D.get(token, 'c_matrix[cv.vocabulary_["{:s}"]].todense()'.format(token))


def rewrite_query(query):
    return " ".join(rewrite_token(token) for token in query.split())


def boolean_search(query):
    hits_matrix = eval(rewrite_query(query))
    hits_list = list(hits_matrix.nonzero()[1])
    print()
    print("Your query ‘{:s}’ matches the following {:d} document:".format(query, len(hits_list)))
    print()
    for i, doc_id in enumerate(hits_list):
        print("Hit #{:d}: document ‘{:s}’: ‘{:.50s}...’".format(i, document_dicts[doc_id]['name'], document_dicts[doc_id]['content']))


def tfidf_cosine_search(query):
    query_vector = tv.transform([query]).tocsc()
    hits = np.dot(query_vector, t_matrix)
    ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse=True)
    print()
    print("Your query ‘{:s}’ matches the following {:d} documents:".format(query, len(ranked_scores_and_doc_ids)))
    print()
    for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
        print("Hit #{:d}: score: {:.4f}: document ‘{:s}’: ‘{:.50s}...’".format(i, score, document_dicts[id]['name'], document_dicts[id]['content']))


if __name__ == '__main__':
    print("Initializing…")
    document_dicts = get_article_dicts()
    documents = [d['content'] for d in document_dicts if 'content' in d]
    cv = CountVectorizer(lowercase=True, binary=True, token_pattern=r'(?u)\b\w\w*\b')
    c_matrix = cv.fit_transform(documents).T.tocsr()
    tv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
    t_matrix = tv.fit_transform(documents).T.tocsr()
    engine = get_engine()
    while True:
        try:
            query = get_lowercase_query()
            if query:
                if engine == "b":
                    boolean_search(query)
                elif engine == "t":
                    tfidf_cosine_search(query)
            else:
                print("Exiting…")
                break
        except KeyError:
            print("Your query produced no results, please try another query.")
