#!/usr/bin/env python3


from flask import Flask, render_template, request
import data
import indexing
import search
import visualisation


app = Flask(__name__)


@app.route('/')
def main():
    query = request.args.get('query')
    matches = []
    if query:
        try:
            pass
        except:
            pass
    return render_template('templates/index.html', matches = matches)


if __name__ == '__main__':
    app.run(debug = False)
