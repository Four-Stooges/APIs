import sys
import pymongo 
from pymongo import MongoClient

client = MongoClient()

usr = sys.argv[1]
pwd = sys.argv[2]
db = client.h_db
#print(usr)
#print(pwd)
user = db.user

try:
    for ele in list(user.find({"name" : usr})): 
        if ele['pwd'] == pwd:
            exit(0)

except:
    exit(2)
exit(1)
