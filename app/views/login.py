import bcrypt

from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for

from app import app

from models import user

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
    if "email" in request.form and "password" in request.form:
        curr_user = user.fetchOneUserPerEmail(request.form["email"])
        if curr_user != None:
            hashed = bcrypt.hashpw(request.form["password"].encode('utf-8'), curr_user.password.encode('utf-8'))
            if hashed == curr_user.password.encode('utf-8'):
                session['id'] = curr_user.id
                flash('You were logged in successfully!')
                return redirect(url_for('index_page'))

    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout_page():
    session.pop('id', None)
    flash('You were logged out')
    return redirect(url_for('login_page'))
