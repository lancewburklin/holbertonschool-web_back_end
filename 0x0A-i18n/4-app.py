#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask
from flask import render_template, request
from flask_babel import Babel, _
app = Flask(__name__)
babel = Babel(app)


class Config:
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def basic_route():
    """ Basic route to index """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    return render_template('4-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
