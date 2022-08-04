
import pymongo


client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
# creating database
database = client['product']
# table creation
collection = database['product_info']

# dataset
productInfo =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
# insert data to mongoDB cloud
collection.insert_many(productInfo)

# retrive records from database
record = collection.find()
for i in record:
    print(i)
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

