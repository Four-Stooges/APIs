import sys
import pymongo 
from pymongo import MongoClient

client = MongoClient()

usr = sys.argv[1]
pwd = sys.argv[2]
db = client.user_db
#print(usr)
#print(pwd)
user = db.user

try:
    for ele in list(user.find({"u_name" : usr})): 
        if ele['u_pwd'] == pwd:
            exit(0)
except Exception:
    exit(2)
exit(1)
