#!/usr/bin/env python3
""" Module of session auth views
"""
from flask.helpers import make_response
from flask import jsonify, abort, request, session
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ Log in user """
    email = request.form.get('email')
    passw = request.form.get('password')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if passw is None or passw == "":
        return jsonify({"error": "password missing"}), 400
    person = User.search({'email': email})
    if person is None or len(person) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    theUser = None
    for per in person:
        if per.is_valid_password(passw):
            theUser = per
    if theUser is None:
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    sess = auth.create_session(theUser.id)
    out = make_response(theUser.to_json())
    out.set_cookie(getenv('SESSION_NAME'), sess)
    return out
