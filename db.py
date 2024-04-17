# db.py
from pymongo import MongoClient

class Database:
    client: MongoClient = None

    @staticmethod
    def initialize():
        # Here, replace 'localhost' with the address of your MongoDB server if it's not on your local machine
        # and adjust the port if necessary (default MongoDB port is 27017).
        Database.client = MongoClient("mongodb://localhost:27017/")
        Database.db = Database.client["fastapi"]  # Access the 'fastapi' database

# Initialize the database when this module is imported
Database.initialize()
