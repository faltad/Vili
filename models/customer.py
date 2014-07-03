
import pymongo

from app import db

def fetchAll(userId, nbCustomers = 10):
    customers = db.customers.find({"userId" : userId}).limit(nbCustomers)
    return customers

def fetchOne(userId, idCustomer):
    customer = db.customers.find_one({"userId" : userId, "id" : idCustomer})
    return customer

def fetchHighestId(userId):
    customer = db.customers.find_one({"userId" : userId}, { "id" : 1, "_id": 0}, sort=[("id", pymongo.DESCENDING)])
    return customer

def insert(userId, newId, title):
    db.customers.insert({"userId" : userId,
                        "id" : newId,
                        "name" : title})

