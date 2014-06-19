
import pymongo

from db import db

def fetchUserInvoices(userId, nbInvoices = 10):
    em = db.get_db()
    invoices = em.invoices.find({"userId" : userId}).limit(nbInvoices)
    return invoices

def fetchOneUserInvoice(userId, idInvoice):
    em = db.get_db()
    invoice = em.invoices.find_one({"userId" : userId, "id" : idInvoice})
    return invoice

def fetchHighestIdUser(userId):
    em = db.get_db()
    invoice = em.invoices.find_one({"userId" : userId}, { "id" : 1, "_id": 0}, sort=[("id", pymongo.DESCENDING)])
    return invoice

def insert(userId, newId, title):
    em = db.get_db()
    em.invoices.insert({"userId" : userId,
                        "id" : newId,
                        "title" : title})


class Invoice():
    def __init__(self):
        self.em = db.get_db()


