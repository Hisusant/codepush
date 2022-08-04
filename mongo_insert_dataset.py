import pymongo
import json
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['ineuron3']
collection = database['fitbit3']

# opening file in r mode and load with json
#with open('fitbit.json', 'r') as fp:
dataset = open('fitbit.json', 'r')
dataset1 = json.load(dataset)
#print(dataset1)

# insert dataset
collection.insert_one(dataset1)

