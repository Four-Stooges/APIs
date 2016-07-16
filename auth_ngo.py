import sys
import pymongo 
from pymongo import MongoClient

client = MongoClient()

usr = sys.argv[1]
pwd = sys.argv[2]
db = client.ngo_db
#print(usr)
#print(pwd)
user = db.user

try:
    for ele in list(user.find({"ngo_name" : usr})): 
        if ele['ngo_pwd'] == pwd:
            exit(0)

except Exception:
    exit(2)
exit(1)
