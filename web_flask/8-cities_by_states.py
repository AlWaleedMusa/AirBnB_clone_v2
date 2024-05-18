#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """close the current SQLAlchemy Session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display an HTML page with a list of all of the State objects"""
    states = storage.all(State).values()
    cities = storage.all(City).values()
    return render_template(
        "8-cities_by_states.html",
        states=states,
        cities=cities
        )


if __name__ == "__main__":
    """main function"""
    app.run(host="0.0.0.0", port=5000)
