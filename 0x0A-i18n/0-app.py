#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', methods=['GET'])
def basic_route():
    """ Basic route to index """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
