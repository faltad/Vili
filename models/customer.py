
import pymongo

from app import db

def fetchAll(userId, nbCustomers = 10):
    customers = db.customers.find({"userId" : userId}).limit(nbCustomers)
    return customers

def fetchOne(userId, idCustomer):
    data = db.customers.find_one({"userId" : userId, "id" : idCustomer})
    customer = Customer(data, db, userId)
    return customer

def fetchHighestId(userId):
    customer = db.customers.find_one({"userId" : userId}, { "id" : 1, "_id": 0}, sort=[("id", pymongo.DESCENDING)])
    return customer

def insert(userId, newId, title):
    db.customers.insert({"userId" : userId,
                        "id" : newId,
                        "name" : title})

def getNew(userId):
    dbInfos = db.customers.find({}, {"id" : 1}).sort("id", -1)
    if dbInfos == None or dbInfos.count() == 0:
        newId = 1
    else:
        newId = int(dbInfos[0]["id"]) + 1

    dbCustomer = dict({"id" : newId})
    customer = Customer(dbCustomer, db, userId)
    return customer

class Customer():
    def __init__(self, dbCustomer, db, userId):
        self.id = dbCustomer["id"]
        self.db = db
        self.userId = userId

        if "name" in dbCustomer:
            self.name = dbCustomer["name"]
        else:
            self.name = ""

        if "address" in dbCustomer:
            self.address = dbCustomer["address"]
        else:
            self.address = ""

        if "city" in dbCustomer:
            self.city = dbCustomer["city"]
        else:
            self.city = ""

        if "country" in dbCustomer:
            self.country = dbCustomer["country"]
        else:
            self.country = ""

    def save(self):
        db.customers.insert({"id" : self.id, "name" : self.name, "address" : self.address, "city" : self.city, "country" : self.country, "userId" : self.userId})

    def update(self):
        db.customers.update({ "id" : self.id }, { '$set' : { "name" : self.name, "address" : self.address, "city" : self.city, "country" : self.country}}, upsert = False)
