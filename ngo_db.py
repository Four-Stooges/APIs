import sys
import pymongo
from pymongo import MongoClient
client=MongoClient()
db=client.ngo_db
ngo=db.ngo
ngo_name=sys.argv[1]
ngo_pwd=sys.argv[2]
mail_id=sys.argv[3]
phone=sys.argv[4]
lat=sys.argv[5]
lng=sys.argv[6]
status=ngo.find({"ngo_name":ngo_name}).count()
if status==0:
	ngo.insert_one({ "ngo_name":ngo_name,"ngo_id":ngo.find().count(),
	              "ngo_pwd":ngo_pwd, "mail_id":mail_id, "ph_no":phone, "ngo_lat":lat,"ngo_lng":lng})
	print(list(ngo.find()))
	exit(0)
else:
	exit(1)	


