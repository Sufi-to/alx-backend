#!/usr/bin/env python3
"""Module for a spinning up a simple flask app with a babel object"""

from flask import Flask, render_template, request
from flask_babel import Babel


@babel.localeselector
def get_locale():
    """Sets the locale language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    """Returns a simple page to render."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
