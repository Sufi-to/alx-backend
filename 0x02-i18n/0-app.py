#!/usr/bin/env python3
"""Module for a spinning up a simple flask app"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Returns a simple page to render."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
