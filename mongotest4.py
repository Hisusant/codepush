import pymongo
import json
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
# print(db)

database = client['product']
collection = database['attribute']

with open('attribute2.json') as fp:
    att_data = json.load(fp)
#print(att_data)
collection.insert_one(att_data)
# insert_one :for json record
# insert_many :for list record
print("insert done...")

'''
#record = collection.find({'status':'A'})
#record = collection.find({'status':{'$in':['A' , 'P']}})
#record = collection.find({'status':{"$gt" : "C"}})
#record = collection.find({'qty':{'$gte' :75}})
#record = collection.find({'item': 'sketch pad','qty': 95})
#record = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})
#record = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})

#collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sushanta'} })
'''