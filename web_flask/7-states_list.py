#!/usr/bin/python3

"""
Module for show list the states
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def displayStates():
    """Show States"""
    all_states = storage.all("State")
    return(render_template(7-states_list.html, State=all_state))

@app.teardown_appcontext
def close(exception=None):
    """Close Method"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
