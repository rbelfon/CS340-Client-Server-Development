# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username="aacuser", password="Quality1!"):
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
       # Complete this create method to implement the C in CRUD.
    def create(self, data):
        try:
            if data is not None:
                self.collection.insert_one(data)
                return True
            else:
                return False
        except Exception:
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        try:
            if query is not None:
                return list(self.collection.find(query))
            else:
                return []
        except Exception:
            return []
            # Update records in the database
    def update(self, query, data):
        try:
            result = self.collection.update_many(query, {"$set": data})
            return result.modified_count
        except Exception:
            return 0

    # Delete records from the database
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception:
            return 0