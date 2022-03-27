#!/usr/bin/env python3


import json


def index(vectorizer, sourcepath):
    with open(sourcepath) as file:
        data_dictionaries = json.load(file)
    documents = [d['forecast text'] for d in data_dictionaries if 'forecast text' in d]
    data_matrix = vectorizer.fit_transform(documents).T.tocsr()
    return data_dictionaries, data_matrix
