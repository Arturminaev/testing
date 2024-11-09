from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus
import pymongo



myclient = pymongo.MongoClient("mongodb+srv://artur544321:Lzim4qI08MOmdAOy@testingcluster.qdmru.mongodb.net/?retryWrites=true&w=majority&appName=testingCluster")

mydb = myclient["sample_mflix"]

mycol = mydb['embedded_movies']
myquery = { "countries": "USA" }
x = mycol.find().limit(2)

print(x)



