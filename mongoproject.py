import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['product']
collection = database['attribute']

with open('attribute2.json') as fp:
    att_data = json.load(fp)
    att_data1 = [att_data]   # convert dict type to list type
collection.insert_many(att_data1)
# insert_many : for list record




'''
# insert_one : for dict record
with open('attribute2.json') as fp:
    att_data = json.load(fp)
#print(att_data)
collection.insert_one(att_data)
'''
print("insert Done...sucess")



