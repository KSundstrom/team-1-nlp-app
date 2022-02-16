#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)

example_data = [{'name': 'Cat', 'content': 'Cat sleeping on a bed'},
                {'name': 'Forest', 'content': 'Misty forest'},
                {'name': 'Bonfire', 'content': 'Bonfire burning'},
                {'name': 'Library', 'content': 'Old library'},
                {'name': 'Orange', 'content': 'Sliced orange'}]


@app.route("/")
def search():
    query = request.args.get('query')
    matches = []
    if query:
        for entry in example_data:
            if query.lower() in entry['name'].lower():
                matches.append(entry)
    return render_template('index.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=False)
