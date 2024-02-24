from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
import pytest


class MongoDatabase:
    """Class holds method for interacting with MongoDB"""

    def __init__(self, connection_uri):
        self.connection = MongoClient(connection_uri)
        self.connection_output = None
        self.db = None
        self.db_list = None
        self.collection_list = None
        self.find_one_result = None
        self.count_result = None
        self.aggregation_result = None

    def test_connection(self):
        """Method for testing connection to MongoDB cluster"""

        try:
            self.connection_output = self.connection.admin.command("ismaster")
            return self.connection_output
        except (ConnectionFailure, OperationFailure) as f:
            pytest.xfail(f"Connection failed. Reason: {str(f)}")
    
    def create_database(self, db_name):
        """Method creates database on MongoDB cluster"""

        self.db = self.connection[db_name]

        return self.db

    def list_databases(self):
        """Method lists database names on cluster"""
        
        self.db_list = self.connection.list_database_names()

        return self.db_list

    def drop_database(self, db_name):
        """Method deletes database on MongoDB cluster"""

        self.connection.drop_database(db_name)
    
    def create_collection(self, collection_name):
        """Method creates collection"""

        self.db[collection_name]

    def list_collections(self):
        """Method lists collections"""

        self.collection_list = self.db.list_collection_names()

        return self.collection_list

    def insert_document_one(self, collection_name, document):
        """Method inserts one document to collection"""

        self.db[collection_name].insert_one(document)

    def select_document_one(self, collection_name, filter):
        """Method selects one document from collection"""

        self.find_one_result = self.db[collection_name].find_one(filter)

        return self.find_one_result
    
    def update_document_one(self, collection_name, filter, values):
        """Method updates one document in collection"""

        self.db[collection_name].update_one(filter, values)

    def delete_document_one(self, collection_name, filter):
        """Method deletes one document from collection"""

        self.db.get_collection(collection_name).delete_one(filter)
    
    def insert_document_many(self, collection_name, document_list):
        """Method inserts many documents to collection"""

        self.db[collection_name].insert_many(document_list)
    
    def count_documents(self, collection_name, filter):
        """Method gets number of documents in collection by specified filter"""

        self.count_result = self.db[collection_name].count_documents(filter)

        return self.count_result
    
    def update_document_many(self, collection_name, filter, update):
        """Method updates many documents"""

        self.db[collection_name].update_many(filter, update)

    def aggregate_documents(self, collection_name, pipeline):
        """Method to work with Mongo aggregation pipeline"""

        self.aggregation_result = self.db[collection_name].aggregate(pipeline)

        return self.aggregation_result
    
    @staticmethod
    def calculate_total_debt_in_uah(aggregation_result, usd_rate, eur_rate):

        total_sum = 0
        for item in aggregation_result:
            if item["_id"] == "UAH":
                total_sum += item["currency_sum"]
            elif item["_id"] == "USD":
                total_sum += item["currency_sum"] * usd_rate
            elif item["_id"] == "EUR":
                total_sum += item["currency_sum"] * eur_rate
        
        return total_sum       
        