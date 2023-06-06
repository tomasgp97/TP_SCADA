from pymongo import MongoClient
import certifi

# MONGO_URI = 'mongodb+srv://manuallende:fBitOOhtHZ4oEJtr@cluster0.mwt0szs.mongodb.net/'
MONGO_URI = "mongodb+srv://tomasgp:tomasgp@scada-registers.gvzsjna.mongodb.net/"

ca = certifi.where()


def db_connection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        # db = client["dbb_peso_app"]
        db = client["clavos"]
        return db
    except ConnectionError as e:
        print('Error connecting to the DB')
        raise e

db_connection()