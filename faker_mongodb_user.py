#!/usr/bin/python
import pymongo
from faker import Faker
import datetime

fake = Faker()
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db = client['test']
collection = db['users']
commentss = db.users
for i in range(300000):
  print(fake.name())
  print(fake.email())
  data = {"uid": i,
            "name": fake.first_name(),
            "surname": fake.last_name(),
			"username": 'user' + str(i),
			"email": fake.email(),
			"location": fake.city(),
			"bio": fake.text(),
			"password": "123456",
            "created_at": datetime.datetime.utcnow()}
  comment_id = commentss.insert_one(data).inserted_id
  print(comment_id)
#Faker Kullanarak 100.000 Adet Fake Data Oluşturuluyor.
