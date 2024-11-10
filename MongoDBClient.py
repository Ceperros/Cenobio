# archivo: MongoDBClient.py

from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
    
    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document)
    
    def find_documents(self, collection_name, query={}):
        collection = self.db[collection_name]
        return collection.find(query)

    def close_connection(self):
        self.client.close()
