
import pymongo

client = pymongo.MongoClient("mongodb+srv://veronicahenaoi:info123@clusterinfo2.8v994es.mongodb.net/?retryWrites=true&w=majority")
db = client.test

mydb = client["bbdd"]
mycol = mydb["clientes"]

#mydict = { "nombre": "Daniela", "direccion": 1 }
#
#x = mycol.insert_one(mydict)
#print(x.inserted_id)

#for x in mycol.find({  "direccion": "C/Mayor, 1" }):
#    print(x)
#
#
myquery = { "nombre": "Luis", "direccion": 12}
newvalues = { "$set": { "edad":25} }

mycol.update_one(myquery, newvalues)
#
##print "clientes" después del update:
#for x in mycol.find():
#  print(x)