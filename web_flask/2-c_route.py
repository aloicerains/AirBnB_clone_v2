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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
