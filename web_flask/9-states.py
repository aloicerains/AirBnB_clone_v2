#!/usr/bin/python3
"""List of states"""

from flask import Flask, render_template
import models
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def li_states(state_id=None):
    """Displays the list of states and cities in alphabet"""
    states = models.storage.all(State)
    if state_id is not None:
        state_id = "State." + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_storage(exception):
    """Closes current Session"""
    models.storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
