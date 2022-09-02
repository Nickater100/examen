from pymongo import MongoClient

client = MongoClient("localhost")

db = client["Examen"]

col = db["tabla"]

print(db.list_database_names())