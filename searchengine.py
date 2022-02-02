#!/usr/bin/env python3


from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup as bs
from urllib import request



 

D = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}

DOCUMENTS = ["This is a silly example",
             "A better example",
             "Nothing to see here",
             "This is a great and long example",
             "That was the real catch-22. The year 1923."]

# Read the database file
content = []
url = "https://www.gutenberg.org/cache/epub/1041/pg1041.txt"
html = request.urlopen(url).read().decode('utf8')


def get_query():
    while True:
        user_input = input("Please enter a query: ")
        query = user_input.strip()
        if query:
            return str(query)
        else:
            return None


def rewrite_token(t):
    return D.get(t, 'sparse_td_matrix[t2i["{:s}"]].todense()'.format(t))


def rewrite_query(query):
    return " ".join(rewrite_token(t) for t in query.split())


if __name__ == '__main__':
        cv = CountVectorizer(lowercase=True, binary=True, token_pattern=r'(?u)\b\w\w*\b') # The pattern now accepts tokens of lenght 1 such as "a"
        sparse_matrix = cv.fit_transform(DOCUMENTS)
        sparse_td_matrix = sparse_matrix.T.tocsr()
        t2i = cv.vocabulary_
        while True:
            try:    
                query = get_query()
                if query is not None:
                    hits_matrix = eval(rewrite_query(query))
                    hits_list = list(hits_matrix.nonzero()[1])
                    for i, doc_idx in enumerate(hits_list):
                        print("Matching doc #{:d}: {:s}".format(i, DOCUMENTS[doc_idx]))
                else:
                    break
            except KeyError:
                print("Your search provided no results, please try another query or hit enter to exit the program.")