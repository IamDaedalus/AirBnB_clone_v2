#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """This method prints Hello HBNB! upon request"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method prints HBNB upon request"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    This method replaces text with whatever text is passed to it. Refer to
    https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    this method replaces <text> with the contents of text or 'is cool' by def
    https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """This method only returns the right page if n is an integer and nothing
    else"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """ This method renders a template html page and dynamically changes
    the value of n based on the number passed here
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
