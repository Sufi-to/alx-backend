#!/usr/bin/env python3
"""Module for a spinning up a simple flask app with a babel object"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get the user from the dictionary"""
    id = request.args.get('login_as')
    return users.get(int(id)) if id else None


@app.before_request
def before_request():
    """Use get_user here"""
    get_user = get_user()
    g.user = get_user


@babel.localeselector
def get_locale():
    """Sets the locale language"""
    return request.args.get('locale') or \
        request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    """Returns a simple page to render."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
