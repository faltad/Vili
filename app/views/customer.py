from functools import wraps
from flask import render_template, redirect, request, session, flash, url_for, abort


from .login import requiresLogin
from app import app

from models import customer
from forms import newCustomerForm

@app.route('/customers/')
@requiresLogin
def customer_index_page():
    custList = customer.fetchAll(session["id"])
    return render_template('list_customers.html', entries=custList)

@app.route('/customers/new', methods=['GET'])
@requiresLogin
def customer_new_page():
    form = newCustomerForm.NewCustomerForm()
    return render_template('new_customer.html', form=form)

@app.route('/customers/new', methods=['POST'])
@requiresLogin
def customer_create_page():
    form = newCustomerForm.NewCustomerForm(request.form)
    if form.validate():
        newCustomer = customer.getNew(session['id'])
        form.populate_obj(newCustomer)
        newCustomer.save()
        flash('The customer has been successfully created!')
        return redirect(url_for("customer_index_page"))
    return render_template('new_customer.html', form=form)

@app.route('/customers/<int:customer_id>', methods=["GET"])
@requiresLogin
def customer_edit_page(customer_id):
    newCustomer = customer.fetchOne(session["id"], customer_id)
    if newCustomer == None:
        abort(404)
    form = newCustomerForm.NewCustomerForm(obj=newCustomer)
    return render_template('edit_customer.html', form=form, customer=newCustomer)

@app.route('/customers/<int:customer_id>', methods=["POST"])
@requiresLogin
def customer_update_page(customer_id):
    newCustomer = customer.fetchOne(session["id"], customer_id)
    if newCustomer == None:
        abort(404)
    form = newCustomerForm.NewCustomerForm(request.form)
    if form.validate():
        form.populate_obj(newCustomer)
        newCustomer.update()
        flash('The customer has been updated')
    return render_template('edit_customer.html', form=form, customer=newCustomer)

