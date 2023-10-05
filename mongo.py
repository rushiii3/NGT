import pymongo
print("hello")
myclient = pymongo.MongoClient("mongodb://localhost:27017")
print(myclient)
#create db
mydb = myclient["rushiDB2"]
#create collection
mycol = mydb["user"]
#insert data
insertUserData = {
    "name":"Vaishali",
    "rollno":"4025A037",
    "dep" : "BCOM",
    "age":30
    }
#print(mycol.insert_one(insertUserData))
#print(myclient.list_database_names())
#print(mydb.list_collection_names())
#fetch user data
fetchdata = mycol.find({"age":{"$gte":20}},{"name":1,"_id":0})
for i in fetchdata:
    print(i["name"], "has age greater than 20")
query = [{"$group":{"_id":"$dep","MaxAge":{"$max":"$age"}}}]
fetchdata = mycol.aggregate(query)
for i in fetchdata:
    print(i)
'''query = {"name":{"$eq":"Rahul"}}
fetchdata = mycol.find(query,{"_id":0,"name":1,"dep":1})
for i in fetchdata:
    print(i)'''
#sort fetchdata
query2 = mycol.find({},{"_id":0,"name":1,"dep":1}).sort("name")
for i in query2:
    print(i)

#delete data
deleteData = mycol.delete_one({"name":"hrushi"})
print(deleteData)


#update data
setAge = {"$set":{"age":30}}
updateData = mycol.update_many({"name":"hrushi"},setAge)
print(updateData.modified_count,"Document Updated")

#drop collection
dropCol = mycol.drop()
print(dropCol)



