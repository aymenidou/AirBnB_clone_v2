#!/usr/bin/python3
"""8. List of states"""
from models import storage, State, Amenity, Place
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def close_session(e):
    """close storage"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_states():
    """fetch all states"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template("100-hbnb.html", states=states, amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
