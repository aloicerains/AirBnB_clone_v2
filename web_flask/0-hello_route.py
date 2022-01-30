#!/usr/bin/python3
"""Hello module"""

from flask import Flask

app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello HBNB

    Returns:
        greetings(str): Hello HBNB!

    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
