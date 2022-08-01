import pymongo
import json
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# print(db)

database = client['product']
collection = database['attribute_table']

with open('attribute2.json') as fp:
    att_data = json.load(fp)
#print(att_data)
collection.insert_one(att_data)

#collection.update_one({'packetType':'D' }, {'$set' : {'packetType': 'E'}})
#collection.delete_one({'packetType': 'E'})
#record = collection.find({'packetType': 'E'})
#for v in record:
 #   print(v)

