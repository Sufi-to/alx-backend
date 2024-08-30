#!/usr/bin/env python3
"""Module for a spinning up a simple flask app with a configed babel object"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    """Returns a simple page to render."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
