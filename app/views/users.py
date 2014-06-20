from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort


from .login import requiresLogin
from app import app

from models import user

@app.route('/profile', methods=['GET'])
@requiresLogin
def profile_page():
    profUser = user.fetchOneById(session["id"])
    return render_template('profile.html', user=profUser, param=profUser)


@app.route('/profile', methods=['POST'])
@requiresLogin
def profile_update_page():
    profUser = user.fetchOneById(session["id"])
    paramData = {
        "surname" : profUser.surname,
        "name" : profUser.name,
        "title" : profUser.title
        }
    errors = {}
    if "surname" in request.form:
        paramData["surname"] = request.form["surname"]
    return render_template('profile.html', user=profUser, param=paramData)

