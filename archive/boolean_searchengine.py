#!/usr/bin/env python3


from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup
from urllib import request
import re


D = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}

ARTICLES_FILE = "data/fiwiki-20181001-corpus.truncated.txt"

SONNETS_URL = "https://www.gutenberg.org/cache/epub/1041/pg1041.txt"


def get_source():
    print()
    while True:
        user_input = input("Please type ‘a’ to use articles or ‘s’ to use sonnets as documents: ")
        if user_input == "a":
            print("Using articles as documents…")
            return "a"
        elif user_input == "s":
            print("Using sonnets as documents…")
            return "s"


def get_articles():
    try:
        with open(ARTICLES_FILE) as file:
            soup = BeautifulSoup(file, 'html.parser')
        articles = []
        for article in soup.find_all('article'):
            articles.append(article.get_text(strip=True))
        return articles
    except OSError:
        print("Error trying to read from file {:s}!".format(ARTICLES_FILE))


def get_sonnets():
    html = request.urlopen(SONNETS_URL).read().decode('utf8')
    newlines_removed = html.replace("\r\n", "#")
    pattern = '((?#*)[IVXLC]+#+)'
    sonnets_hash = re.split(pattern, newlines_removed)
    sonnets = []
    for sonnet in sonnets_hash:
        sonnet = sonnet.replace("#", "")
        sonnets.append(sonnet)
    return sonnets


def get_query():
    print()
    return input("Please enter a query or press enter to exit: ").strip()


def rewrite_token(t):
    return D.get(t, 'sparse_td_matrix[cv.vocabulary_["{:s}"]].todense()'.format(t))


def rewrite_query(query):
    return " ".join(rewrite_token(t) for t in query.split())


def main():
    cv = CountVectorizer(lowercase=True, binary=True, token_pattern=r'(?u)\b\w\w*\b')
    source = get_source()
    if source == "a":
        documents = get_articles()
    elif source == "s":
        documents = get_sonnets()
    sparse_matrix = cv.fit_transform(documents)
    sparse_td_matrix = sparse_matrix.T.tocsr()
    while True:
        try:
            query = get_query()
            if query:
                hits_matrix = eval(rewrite_query(query))
                hits_list = list(hits_matrix.nonzero()[1])
                for i, doc_idx in enumerate(hits_list):
                    print("Matching doc #{:d}: {:s}".format(i, documents[doc_idx]))
                    print()
            else:
                break
        except KeyError:
            print("Your search provided no results, please try another query.")


if __name__ == '__main__':
    main()
