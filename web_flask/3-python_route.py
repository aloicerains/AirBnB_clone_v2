#!/usr/bin/python3
"""Hello module"""

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_hbnb(strict_slashes=False):
    """Hello HBNB

    Returns:
        greetings(str): Hello HBNB!

    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb(strict_slashes=False):
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<path:subpath>')
def display_subpath(subpath, strict_slashes=False):
    """Displays c/text"""
    return 'C {}'.format(subpath.replace('_', ' '))


@app.route('/python/<path:subpath>')
def python_path(subpath, strict_slashes=False):
    """Display the subpath Python"""
    return 'Python {}'.format(subpath.replace('_', ' '))


@app.route('/python/')
def python_pathless(strict_slashes=False):
    """Display the default option"""
    return 'Python is cool'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
