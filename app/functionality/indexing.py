#!/usr/bin/env python3


import json


def index(vectorizer, sourcepath):
    with open(sourcepath) as file:
        data_dictionaries = json.load(file)
    data_list = [' '.join([d['date'], d['title'], d['place'], d['forecast'], d['forecast text']]) for d in data_dictionaries]
    data_matrix = vectorizer.fit_transform(data_list).T.tocsr()
    return data_dictionaries, data_matrix
