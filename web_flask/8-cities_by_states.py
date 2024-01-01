#!/usr/bin/python3
"""8. List of states"""
from models import storage, State, City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(e):
    """close storage"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """fetch all states"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
