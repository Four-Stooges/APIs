try:
	import sys
	import pymongo
	from pymongo import MongoClient
	client=MongoClient()
	db=client.user_db
	u_name=sys.argv[1]
	u_pwd=sys.argv[2]
	f_name=sys.argv[3]
	l_name=sys.argv[4]
	ph_no=sys.argv[5]
	user=db.user
	status=user.find({"u_name":u_name}).count()
	if status==0:
		user.insert_one({"user_id":user.find().count(),  "u_name":u_name,  "u_pwd":u_pwd,"f_name":f_name,"l_name":l_name,"uploads":[]})
		print(list(user.find()))
		exit(0)
	else:
 		exit(1)
  	 
except Exception:
	exit(2)        	
  
