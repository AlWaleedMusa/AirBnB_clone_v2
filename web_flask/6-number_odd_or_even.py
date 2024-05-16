
#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This function returns a string when the route / is hit"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """This function returns a string when the route /hbnb is hit"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """This function returns a string when the route /c/<text> is hit
    and replacing _ with spaces"""
    return "C " + text.replace("_", " ")

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python_is_cool(text="is cool"):
    """This function returns a string when the route /python/<text> is hit
    and replacing _ with spaces"""
    return "Python " + text.replace("_", " ")

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """This function returns a string when the route /number/<n> is hit
    and n is an integer"""
    return "{} is a number".format(n) if isinstance(n, int) else None

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """This function returns a string when the route /number_template/<n> is hit
    and n is an integer"""
    return render_template("5-number.html", n=n) if isinstance(n, int) else None

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """This function returns a string when the route /number_odd_or_even/<n> is hit
    and n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n, type="even" if n % 2 == 0 else "odd")


if __name__ == "__main__":
    app.run()
