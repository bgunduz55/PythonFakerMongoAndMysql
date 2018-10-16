#!/usr/bin/python
import pymongo
from faker import Faker
import datetime

fake = Faker()
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['test']
collection = db['post']
commentss = db.post
for i in range(300000):
  print(fake.name())
  print(fake.email())
  data = {"userid": i,
            "post": fake.text(),
            "location": fake.city(),
            "created_at": datetime.datetime.utcnow()}
  comment_id = commentss.insert_one(data).inserted_id
  print(comment_id)
#Faker Kullanarak 100.000 Adet Fake Data Oluşturuluyor.
