import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://David05:<password>@cluster0.vd7bg6q.mongodb.net/?retryWrites=true&w=majority")
db = client ["test"]
collection = db ["test"]

diccionario = [
  {  "id": 1, "nombre":  "xopa", "significado":  "es saludar a un amigo"},
  {  "id": 2, "nombre":  "chantin", "significado":  "se refiere a una casa"},
  {  "id": 3, "nombre":  "mopri", "significado":  "es decir primo alrevez"},
  {  "id": 4, "nombre":  "yeye", "significado":  "persona de alta clase"},
  {  "id": 5, "nombre":  "pelaito", "significado":  "es un niño"},
]
    
collection.insert_one(diccionario)
collection.delete_one({"id:4"})
collection.update_many({"id": 4, "nombre":  "yeye", "significado":  "persona de alta clase"})


