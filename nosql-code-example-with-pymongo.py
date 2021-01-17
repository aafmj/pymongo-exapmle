"""
pymongo: https://www.w3schools.com/python/python_mongodb_getstarted.asp
mongodb: https://docs.atlas.mongodb.com/getting-started/

"""


import pymongo


# Setup Connections
password = "mongo-test_972023022_1"
db_name = ""  # optinal
client = pymongo.MongoClient("mongodb+srv://mongo-test:"+password+"@cluster0.tigpf.mongodb.net/"+db_name+"?retryWrites=true&w=majority")

mydb = client["db1"]

mycol = mydb["customers"]











# ================= INSERT ~ INSERT =================
mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)


mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

obj = mycol.insert_many(mylist)

# print list of the _id values of the inserted documents:
print(obj)















# ================= FIND ~ SELECT =================
# first_occurrencerst_doc = mycol.find_one()
# print(first_occurrencerst_doc)

# all_docs = mycol.find()
# for x in all_docs:
#   print(x)

myquery = {}
# myquery = { "address": "Park Lane 38" }
# myquery = { "address": { "$gt": "S" } }
# myquery = { "address": { "$regex": "^S" } }

# mydoc = mycol.find(myquery, { "_id": 0, "name": 1, "address": 1 }).sort("name", -1).limit(5)
# for x in mydoc:
#   print(x)














# ================= UPDATE ~ UPDATE =================
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Canyon 123" } }
# mycol.update_one(myquery, newvalues)
# for x in mycol.find():
#   print(x)

# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

















# ================= DELETE ~ DELETE =================
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

mycol.drop()