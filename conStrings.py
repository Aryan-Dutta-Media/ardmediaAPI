import os
from pymongo import MongoClient
try:
    conn=os.environ.get('DATABASE_URI')
except:
    print('CANNOT CONNECT TO DATABSE')
client=MongoClient(conn)
db1=client.adrmedia