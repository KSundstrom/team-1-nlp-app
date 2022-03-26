#!/usr/bin/env python3


from bs4 import BeautifulSoup as bs
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


ARTICLES_FILE = "data/enwiki-20181001-corpus.1000-articles.txt"


document_dicts = []
with open(ARTICLES_FILE) as file:
    soup = bs(file, 'lxml')
for article in soup.find_all('article'):
    document_dicts.append({'name':article['name'], 'content':article.get_text(strip=True)})
documents = [d['content'] for d in document_dicts if 'content' in d]
tv = TfidfVectorizer(lowercase=True, sublinear_tf=True, use_idf=True, norm="l2")
t_matrix = tv.fit_transform(documents).T.tocsr()


def search_dict():
    query = input("Search for: ")
    matches = []
    if query:
        try:
            query_vector = tv.transform([query]).tocsc()
            hits = np.dot(query_vector, t_matrix)
            ranked_scores_and_doc_ids = sorted(zip(np.array(hits[hits.nonzero()])[0], hits.nonzero()[1]), reverse=True)
            for i, (score, id) in enumerate(ranked_scores_and_doc_ids):
                matches.append({'hit':"{:d}".format(i+1), 'score':"{:.4f}".format(score), 'name':"{:s}".format(document_dicts[id]['name']), 'content':"{:.100s}…".format(document_dicts[id]['content'])})
        except:
            pass
    return matches

def visualise_search(input_dict):
    import seaborn as sns
    import pandas as pd
    import numpy as np 
    import matplotlib.pyplot as plt

    matches_df = pd.DataFrame.from_dict(input_dict)
    #sns.set_theme()
    plot = sns.lineplot(
        data=matches_df,
        x = "hit",
        y = "score",
    )

    for ind, label in enumerate(plot.get_xticklabels()):
        if ind % 10 == 0:  # every 10th label is kept
            label.set_visible(True)
        else:
            label.set_visible(False)

    #plot.set(yticks=np.arange(0, 1, step= 0.01))

    return plt.show()



if __name__ == "__main__":
    matches = search_dict()
    visualise_search(matches)

