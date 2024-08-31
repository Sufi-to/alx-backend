#!/usr/bin/env python3
"""Module for a spinning up a simple flask app with a babel object"""

import pytz
from datetime import datetime
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime


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
    user_obj = get_user()
    g.user = user_obj


@babel.localeselector
def get_locale():
    """Sets the locale language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Infer the appropriate time zone"""
    if request.args.get('timezone'):
        time_zone = request.args.get('timezone', None)
    elif g.user:
        time_zone = g.user.get('timezone', None)

    if time_zone:
        try:
            selected_timezone = pytz.timezone(time_zone)
            return selected_timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world():
    """Returns a simple page to render."""
    now_utc = datetime.utcnow()
    local_time = now_utc.replace(tzinfo=pytz.utc).astimezone(
        pytz.timezone(get_timezone())
        )
    formatted_time = format_datetime(local_time)
    return render_template('index.html', local_time=formatted_time)


if __name__ == '__main__':
    app.run()
