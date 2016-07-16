import math as m
import sys
import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.ngo_data
user=db.user           #collection for new ngo database.
db2=client.ngo_db      #db variable for colletion.
ngo=db2.ngo
person_lat=int(sys.argv[1])
person_long=int(sys.argv[2])
for ele in list(ngo.find()):
	lat=int(ele['ngo_lat'])
	lng=int(ele['ngo_lng'])
	#print(lat)
	#print(lng)
	
	dist=((lat - person_lat)**2 + (lng - person_long)**2)**0.5
	user.insert_one({"ngo_id":ele['ngo_id'],"status":"Pd","dist":dist})
	
for ele in user.find().sort('dist',pymongo.ASCENDING):
	x=ele['ngo_id']                   #selected ngo.
	break

data=client.person_db
pid=data.user
for jamaal in pid.find():
	jamal_id=jamaal['person_id']
	
	with open("ngodata.txt", "a") as myfile:
	    myfile.write(str(x) + "\t" + str(jamal_id) +"\n")


	
