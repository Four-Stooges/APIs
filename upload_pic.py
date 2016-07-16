import sys
import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.person_db
user=db.user
img_id=sys.argv[1]
lat=sys.argv[2]
lng=sys.argv[3]
#ele = user.find()
#cnt=user.find().count()
for ele in user.find():
	#res=cmp_img_id.py
	res=0
	if res==0:
		icount = int(ele['count']) + 1
		result_id = str(ele['person_id'])
		user.update_one({"person_id":result_id},{'$set':{"lat":lat,"long":lng,
		                "count": str(icount)}},upsert=True)
		if icount >3:
			user.update_one({"person_id":result_id},{'$set':{"status":"Pd"}},upsert=True)	                
	else:
		user.insert_one({"person_id":img_id,"lat":lat,"long":lng,"count":1,
		                "status":"P"}) 
		

		
		
