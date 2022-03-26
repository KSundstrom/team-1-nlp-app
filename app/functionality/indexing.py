#!/usr/bin/env python3


from bs4 import BeautifulSoup as bs


def main(vectorizer, sourcepath):
    document_dictionaries = []
    with open(sourcepath) as file:
        soup = bs(file, 'lxml')
    for article in soup.find_all('article'):
        document_dictionaries.append({'name':article['name'], 'content':article.get_text(strip=True)})
    documents = [d['content'] for d in document_dictionaries if 'content' in d]
    document_matrix = vectorizer.fit_transform(documents).T.tocsr()
    return document_dictionaries, document_matrix
