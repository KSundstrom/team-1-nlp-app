#!/usr/bin/env python3


import numpy as np


def search(vectorizer, data_dictionaries, data_matrix, query):
    matches = []
    query_vector = vectorizer.transform([query]).tocsc()
    hits = np.dot(query_vector, data_matrix)
    ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse = True)
    for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
        matches.append({'hit':"{:d}".format(i+1), 'score':"{:.4f}".format(score), 'date':"{:s}".format(data_dictionaries[id]['date']), 'title':"{:s}".format(data_dictionaries[id]['title']), 'place':"{:s}…".format(data_dictionaries[id]['place']), 'forecast':"{:s}…".format(data_dictionaries[id]['forecast']), 'forecast text':"{:s}".format(data_dictionaries[id]['forecast text'])})
    return matches
