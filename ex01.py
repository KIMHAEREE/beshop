from pymongo import MongoClient
from bson.json_util import dumps
client = MongoClient('localhost', 27017)
mydb = client.bit
mycol = mydb.student
#s = {"name":"김슬지","kor":100,"eng":80,"math":90}
for s in mycol.find({"kor":{"$gt":80}},{"_id":0,"name":1,"kor":1}):
    print(s)