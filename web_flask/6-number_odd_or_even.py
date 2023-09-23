#!/usr/bin/python3
"""A script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return a given text"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Diplays a given text"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns a given text and replaces _with "" """
    return ("C {}".format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Returns a given text"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display a number if it's an int"""
    if isinstance(n, int):
        return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        if n % 2:
            eo = "odd"
        else:
            eo = "even"
        return render_template("6-number_odd_or_even.html", n=n, eo=eo)


if __name__ == "__main__":
    app.run()
