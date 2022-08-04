import pymongo
#import json
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#print(db)

database = client['ineuron2']
collection = database['fitbit2']

record = collection.find()
for i in record:
    print(i)

#print(i)