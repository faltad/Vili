from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort


from .login import requiresLogin
from app import app

@app.route('/profile')
@requiresLogin
def profile_page():
    
