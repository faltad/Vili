
from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for

from db import db

from .login import requiresLogin
from app import app

from models import invoice

@app.route('/')
@requiresLogin
def index_page():
    return render_template('dashboard.html')

