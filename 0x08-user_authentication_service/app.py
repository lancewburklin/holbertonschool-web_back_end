#!/usr/bin/env python3
""" Flask application """
from flask import Flask
from flask import jsonify, request, abort, make_response
from auth import Auth
app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'])
def basic_route():
    """ Basic route test """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def create_user():
    """ Create the user """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_user = AUTH.register_user(email, password)
        val = {"email": "{}".format(email), "message": "user created"}
        return jsonify(val)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ Log the user in with session ID """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    new_sess = AUTH.create_session(email)
    res_t = {"email": "{}".format(email), "message": "logged in"}
    res = make_response(jsonify(res_t))
    res.set_cookie("session_id", new_sess)
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
