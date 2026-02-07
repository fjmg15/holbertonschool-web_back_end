#!/usr/bin/env python3
"""
Provide stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    print(f"\tmethod GET: {collection.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {collection.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {collection.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {collection.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {collection.count_documents({'method': 'DELETE'})}")

    print(f"{collection.count_documents({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    log_stats()
