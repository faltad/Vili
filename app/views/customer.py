from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort


from .login import requiresLogin
from app import app

from models import customer

@app.route('/customers/')
@requiresLogin
def customer_index_page():
    custList = customer.fetchAll(session["id"])
    return render_template('list_customers.html', entries=custList)

@app.route('/customers/new', methods=['GET'])
@requiresLogin
def customer_new_page():
    entry = customer.fetchHighestId(session["id"])
    if entry == None:
        new_id = 1
    else:
        new_id = entry["id"] + 1
    return render_template('new_customer.html', new_id=new_id, errors={})

@app.route('/customers/new', methods=['GET'])
@requiresLogin
def customer_create_page():
    entry = customer.fetchHighestId(session["id"])
    if entry == None:
        new_id = 1
    else:
        new_id = entry["id"] + 1
    return render_template('new_customer.html', new_id=new_id, errors={})

