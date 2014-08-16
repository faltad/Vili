from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort

from .login import requiresLogin
from app import app

from models import invoice
from models import user

@app.route('/invoices/')
@requiresLogin
def invoice_index_page():
    entries = invoice.fetchUserInvoices(session["id"])
    return render_template('list_invoices.html', entries=entries)

@app.route('/invoices/<int:invoice_id>')
@requiresLogin
def invoice_view_page(invoice_id):
    entry = invoice.fetchOneUserInvoice(session["id"], invoice_id)
    profUser = user.fetchOneById(session["id"])
    if entry == None:
        abort(404)
    return render_template('invoice.html', entry=entry, user=profUser)

@app.route('/invoices/new', methods=['GET'])
@requiresLogin
def invoice_new_page():
    entry = invoice.fetchHighestIdUser(session["id"])
    if entry == None:
        new_id = 1
    else:
        new_id = entry["id"] + 1
    return render_template('new_invoice.html', new_id=new_id, errors={})

@app.route('/invoices/new', methods=['POST'])
@requiresLogin
def invoice_create_page():
    errors = {}
    entry = invoice.fetchHighestIdUser(session["id"])
    if "id" in request.form and "title" in request.form:
        if entry == None:
            highest_id = 0
        else:
            highest_id = entry["id"]
        new_id = int(request.form["id"])
        if highest_id >= new_id:
            errors["id"] = True
        if len(request.form["title"]) < 1:
            errors["title"] = True
        if len(errors) == 0:
            invoice.insert(session["id"], new_id, request.form["title"])
            return redirect(url_for("invoice_view_page", invoice_id=new_id))
    else:
        errors["total"] = True

    new_id = entry["id"] + 1

    return render_template('new_invoice.html', errors=errors, new_id = new_id)


