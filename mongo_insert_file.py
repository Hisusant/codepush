import pymongo
import json
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['ineuron2']
collection = database['fitbit2']

# opening file in r mode and load with json
with open('fitbit.json', 'r') as fp:
    fitbit_data = json.load(fp)
    #print(fitbit_data)

# insert dataset
collection.insert_one(fitbit_data)
