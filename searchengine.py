#!/usr/bin/env python3


from sklearn.feature_extraction.text import CountVectorizer


D = {"and": "&", "AND": "&",
     "or": "|", "OR": "|",
     "not": "1 -", "NOT": "1 -",
     "(": "(", ")": ")"}

DOCUMENTS = ["This is a silly example",
             "A better example",
             "Nothing to see here",
             "This is a great and long example"]

QUERY = "NOT example OR great"


def rewrite_token(t):
    return D.get(t, 'sparse_td_matrix[t2i["{:s}"]].todense()'.format(t))


def rewrite_query(query):
    return " ".join(rewrite_token(t) for t in query.split())


if __name__ == '__main__':
    cv = CountVectorizer(lowercase=True, binary=True)
    sparse_matrix = cv.fit_transform(DOCUMENTS)
    sparse_td_matrix = sparse_matrix.T.tocsr()
    t2i = cv.vocabulary_
    hits_matrix = eval(rewrite_query(QUERY))
    hits_list = list(hits_matrix.nonzero()[1])
    for i, doc_idx in enumerate(hits_list):
        print("Matching doc #{:d}: {:s}".format(i, DOCUMENTS[doc_idx]))
