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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
