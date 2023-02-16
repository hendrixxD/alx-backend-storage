from pymongo import MongoClient

# creating pymongo Client
client = MongoClient('localhost', 27017)

# database instanxe
db = client['mydb']
print("database created....")

# verification
print("list of databases after creating new one")
print(client.list_database_names())
