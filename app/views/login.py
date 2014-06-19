import bcrypt

from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for

from app import app
from db import db


def requiresLogin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'id' not in session or not session["id"]:
            return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['GET'])
def login_page():
    if session.get('id'):
        return redirect(url_for('index_page'))

    error = None
    return render_template('login.html', error=error)

@app.route('/login', methods=['POST'])
def try_login_page():
    if session.get('id'):
        return redirect(url_for('index_page'))

    error = True
    if "username" in request.form and "password" in request.form:
        em = db.get_db()
        user = em.users.find_one({'name' : request.form["username"] })
        if user != None:
            hashed = bcrypt.hashpw(request.form["password"].encode('utf-8'), user["password"].encode('utf-8'))
            if hashed == user["password"].encode('utf-8'):
                session['id'] = user["id"]
                flash('You were logged in successfully!')
                return redirect(url_for('index_page'))

    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout_page():
    session.pop('id', None)
    flash('You were logged out')
    return redirect(url_for('login_page'))
