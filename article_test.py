#!/usr/bin/env python3


from sklearn.feature_extraction.text import CountVectorizer
from bs4 import BeautifulSoup


D = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}

ARTICLES_FILE = "data/enwiki-20181001-corpus.1000-articles.txt"


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


def get_query():
    print()
    return input("Please enter a query or press enter to exit: ").strip()


def rewrite_token(t):
    return D.get(t, 'sparse_td_matrix[cv.vocabulary_["{:s}"]].todense()'.format(t))


def rewrite_query(query):
    return " ".join(rewrite_token(t) for t in query.split())


def main():
    cv = CountVectorizer(lowercase=True, binary=True, token_pattern=r'(?u)\b\w\w*\b')
    documents = get_articles()
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
