#!/usr/bin/python

from faker import Faker
import pymysql

fake = Faker()

for i in range(100000):
  print(fake.name())
  print(fake.email())
  print(i)
  # Ekleme Sorgusu Çalışıyor.
  try:
      baglanti = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = '123456Bg', db = 'springdata1', autocommit=True)
      baglanti = baglanti.cursor()
      baglanti.execute('SET NAMES UTF8')
  except:
      print("Veritabanı Bağlantı Hatası")
      exit()

  # Sorgu oluşturuluyor
  try:
      sorgu = "INSERT INTO users (name, surname, username, email, bio, password, created_at) VALUES ('{adi}', '{soyadi}', '{username}', '{mail}', '{bio}', '{sifre}', '{date}')".format(adi = fake.first_name(), soyadi = fake.last_name(), username = 'user' + str(i), mail = fake.email(), bio = "", sifre = fake.password(), date = fake.date_time())
      # sorgu = "INSERT INTO feelings (user_id, feel) VALUES (1,'asdasd')"
      baglanti.execute(sorgu)
  except Exception as e:
      print(e)
      pass

  # Sorgu veritabanına gönderildi.
  # Eklenen kayıta ait satır numarası
  finally:
    sorgu_satiri = baglanti.lastrowid
    print("Kullanıcı eklendi, eklenen satır ID'si {id}".format(id = sorgu_satiri))
    baglanti.close()

  # Bağlantı Kapatıldı.
  
#Faker Kullanarak 100.000 Adet Fake Data Oluşturuluyor.
