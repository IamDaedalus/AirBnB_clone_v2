#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
