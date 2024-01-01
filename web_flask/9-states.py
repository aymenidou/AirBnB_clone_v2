#!/usr/bin/python3
"""8. List of states"""
from models import storage, State, City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(e):
    """close storage"""
    storage.close()


@app.route("/states", strict_slashes=False)
def display_states():
    """fetch all states"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states, cities=None)


@app.route("/states/<id>", strict_slashes=False)
def display_states(id):
    """fetch all states"""
    state_id = "State." + id
    states = storage.all(State)
    if (state_id in states):
        states = states[state_id]
    return render_template("9-states.html", states=states, cities="show")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
