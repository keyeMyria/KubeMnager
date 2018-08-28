from django.db import models
from pymongo import MongoClient
from pprint import pprint

# Create your models here.
host = 'localhost'
username = 'liuzhi'
password = '968385'
db_name = 'kubernetes'
client = MongoClient('localhost:27017', username='liuzhi', password='968385', authSource='kubernetes')
kubernetes_db = client.get_database('kubernetes')


