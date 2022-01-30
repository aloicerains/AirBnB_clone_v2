#!/usr/bin/python3
"""HBNB flask applications"""

from flask import Flask, render_template
import models
from models import *


app = Flask(__name__)
@app.route('/hbnb_filters', strict_slashes=False)
def index():
    """Displays the index files"""
    states = models.storage.all(State).values()
    amenities = models.storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes current Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
