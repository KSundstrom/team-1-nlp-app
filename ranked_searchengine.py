#!/usr/bin/env python3


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup
from urllib import request
import re
import numpy as np


D = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}

ARTICLES_FILENAME = "fiwiki-20181001-corpus.truncated.txt"



tfv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
cv = CountVectorizer(lowercase=True)

def get_articles():
    try:
        with open(ARTICLES_FILENAME) as file:
            soup = BeautifulSoup(file, 'html.parser')
        articles = []
        for article in soup.find_all('article'):
            articles.append(article.get_text(strip=True))
        return articles
    except OSError:
        print("Error trying to read from file {:s}!".format(ARTICLES_FILENAME))

def get_query():
    print()
    return input("Please enter a query or press enter to exit: ").strip()


def get_hits(query):
    query_as_words = query.split(" ")
    hit_list = []
    for word in query_as_words:
        hit_list = np.array.sum(hit_list, tf_matrix[t2i[query]])
    hits_and_doc_ids = [ (hits, i) for i, hits in enumerate(hit_list) if hits > 0 ]
    ranked_hits_and_doc_ids = sorted(hits_and_doc_ids, reverse=True)
    return ranked_hits_and_doc_ids

if __name__ == '__main__':
    t2i = cv.vocabulary_
    articles = get_articles()
    tf_matrix = tfv.fit_transform(articles).T.todense()
    while True:
        try:
            query = get_query()
            if query:
                article_hits = get_hits(query)
                for hit, i in article_hits:
                    print(f"Score of '{query}' is {hit}")
            else:
                break
        except KeyError:
            print("Your search provided no results, please try another query.")
    
