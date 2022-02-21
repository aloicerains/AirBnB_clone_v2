#!/usr/bin/python3
"""List of states"""

from flask import Flask, render_template
import models
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_city_states():
    """Displays the list of states"""
    states = models.storage.all(State).values()
    # states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes current Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
