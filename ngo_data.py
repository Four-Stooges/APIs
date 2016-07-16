import math as m
import sys
import pymongo
from pymongo import MongoClient()
client=MongoClient()
db=client.ngo_data
user=db.user           #collection for new ngo database.
db2=client.ngo_db      #db variable for colletion.
ngo=db2.ngo
person_lat=sys.argv[1]
person_long=sys.argv[2]
for ele in list(ngo.find()):
	lat=ele['ngo_lat']
	lng=ele['ngo_lng']
	dist=m.sqrt((lat-person_lat)**2+(lng-person_lng)**2)
	user.insert_one({"ngo_id":ngo_id,"status":"r","dist":dist})
	
for ele in user.find().sort('dist',pymongo.ASCENDING):
	x=ele['ngo_id']
	break	
	
