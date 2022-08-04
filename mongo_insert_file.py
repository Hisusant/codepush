import pymongo
import json
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
#db = client.test
#print(db)

database = client['ineuron2']
collection = database['fitbit2']

# opening file in r mode and load with json
dataset = open('fitbit.json', 'r')
dataset2 = json.load(dataset)
#print(dataset2)

# insert dataset
collection.insert_one(dataset2)

'''
# insert_many use when we have list data: 
dataset2 = json.load(dataset)
dataset3=[dataset2]
collection.insert_many(dataset3)
'''