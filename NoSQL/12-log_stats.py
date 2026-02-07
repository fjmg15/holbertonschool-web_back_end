#!/usr/bin/env python3
"""
Provide stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def log_stats():
    try:
        client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=2000)
        collection = client.logs.nginx

        print(f"{collection.count_documents({})} logs")

        print("Methods:")
        print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
        print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
        print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
        print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
        print(f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")

        print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")

    except ServerSelectionTimeoutError:
        # MongoDB not running → do not crash
        print("0 logs")
        print("Methods:")
        print("\tmethod GET: 0")
        print("\tmethod POST: 0")
        print("\tmethod PUT: 0")
        print("\tmethod PATCH: 0")
        print("\tmethod DELETE: 0")
        print("0 status check")


if __name__ == "__main__":
    log_stats()
