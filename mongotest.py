import pymongo
client = pymongo.MongoClient("mongodb+srv://Prabhat:pr171219#@prabhat-cluster0.szwyq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"prabhat1",
    "email" : "prabhat1@gmail.com",
    "surname" : "kumar"
}
d = {
    "name":"prabhat1",
    "email" : "prabhat1@gmail.com",
    "surname" : "kumar"
}
db1 = client['mongotest1']
coll = db1['test']
# coll.insert_one(d)