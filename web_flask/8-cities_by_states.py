#!/usr/bin/python3
"""8. List of states"""
from models import storage, State, City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(e):
    """close storage"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """fetch all states"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
