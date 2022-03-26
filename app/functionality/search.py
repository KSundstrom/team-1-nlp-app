#!/usr/bin/env python3


import numpy as np


def search(vectorizer, document_dictionaries, document_matrix, query):
    matches = []
    query_vector = vectorizer.transform([query]).tocsc()
    hits = np.dot(query_vector, document_matrix)
    ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse = True)
    for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
        matches.append({'hit':"{:d}".format(i+1), 'score':"{:.4f}".format(score), 'name':"{:s}".format(document_dictionaries[id]['name']), 'content':"{:.100s}…".format(document_dictionaries[id]['content'])})
    return matches
