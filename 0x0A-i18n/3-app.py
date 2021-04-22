#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask
from flask import render_template, request
from flask_babel import Babel, _
app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config settings for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Get location and select best language """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'])
def basic_route():
    """ Basic route to index """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
