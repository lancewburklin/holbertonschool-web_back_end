#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask
from flask import render_template, request, g
from flask_babel import Babel, _, gettext
from typing import Dict
app = Flask(__name__)
babel = Babel(app)


@app.before_request
def before_request():
    """ Check if a user logged in """
    user = get_user()
    if user is not None:
        g.user = user
    else:
        g.user = None


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """ Get a user from argument """
    user = request.args.get('login_as')
    if user is None:
        return None
    return users.get(int(user))


class Config:
    """ Config settings for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get location and select best language """
    lang = request.args.get('locale')
    if lang is not None and lang in app.config['LANGUAGES']:
        return lang
    if g.user is not None:
        if g.user.get('locale') in app.config['LANGUAGES']:
            return g.user.get('locale')
    lang = request.headers.get('Accept-Language')
    if lang is not None and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def basic_route():
    """ Basic route to index """
    home_title = _("home_title")
    home_header = _("home_header")
    user = g.user
    if user is not None:
        logged_in_as = _('logged_in_as', username=user.get('name'))
        res = logged_in_as
    else:
        not_logged_in = gettext(u'not_logged_in')
        res = not_logged_in
    return render_template('6-index.html', home_title=home_title,
                           home_header=home_header, log=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
