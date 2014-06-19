
import pymongo

from app import db

def fetchUserInvoices(userId, nbInvoices = 10):
    print(db)
    invoices = db.invoices.find({"userId" : userId}).limit(nbInvoices)
    return invoices

def fetchOneUserInvoice(userId, idInvoice):
    invoice = db.invoices.find_one({"userId" : userId, "id" : idInvoice})
    return invoice

def fetchHighestIdUser(userId):
    invoice = db.invoices.find_one({"userId" : userId}, { "id" : 1, "_id": 0}, sort=[("id", pymongo.DESCENDING)])
    return invoice

def insert(userId, newId, title):
    db.invoices.insert({"userId" : userId,
                        "id" : newId,
                        "title" : title})


