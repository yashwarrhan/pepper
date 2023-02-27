from pymongo import MongoClient


def get_db_handle(db_name, host='localhost', port=27017):
    client = MongoClient(host=host, port=int(port))
    db_handle = client[db_name]
    return db_handle


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
