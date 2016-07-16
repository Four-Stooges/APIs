import sys
import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.person_db
user=db.user
img_id=sys.argv[1]
lat=sys.argv[2]
lng=sys.argv[3]
for ele in user.find():
	res=cmp_img_id.py
	if res==0:
		user.update_one(filter=None,{'$set':{"lat":lat,"long":lng}}
		                {'$inc':{"count": 1}})
	if ele['count']>3:
		user.update_one(filter=None,{'$set':{"status":"Pd"}})	                
	else:
		user.insert_one({"person_id":img_id,"lat":lat,"long":lng,"count":1,
		                "status":"P"}) 
		

		
		
