import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['product']
collection = database['product_details']

with open('attribute2.json') as fp:
    att_data = json.load(fp)
collection.insert_many(att_data)

