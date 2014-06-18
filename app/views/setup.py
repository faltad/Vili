
from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for

from app import app

@app.route('/setup')
def setup_page():
    if app.config["install"] == True:
        return redirect(url_for('index_page'))
    return render_template('setup.html')
