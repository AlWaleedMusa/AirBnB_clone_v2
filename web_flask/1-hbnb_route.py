#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This function returns a string when the route / is hit"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function returns a string when the route /hbnb is hit"""
    return "HBNB"


if __name__ == "__main__":
    """main function"""
    app.run()
