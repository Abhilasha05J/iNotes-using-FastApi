from pymongo import MongoClient
MONGO_URI = "mongodb+srv://Cluster80728:cFNhVUN5R3lz@cluster80728.ymaek.mongodb.net"

try:
    conn = MongoClient(MONGO_URI)
    print("Database connected")
except Exception as e:
    print(f"Failed to connect: {e}")
