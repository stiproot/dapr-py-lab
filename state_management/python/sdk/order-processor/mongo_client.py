import os
import json
import uuid
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

# MONGO_HOST = os.getenv('MONGO_HOST', 'mongo')
# MONGO_PORT = os.getenv('MONGO_PORT', '27017')

MONGO_HOST = 'mongo'
MONGO_PORT = '27017'

# Connect to MongoDB without authentication
client = MongoClient(MONGO_HOST, int(MONGO_PORT))
db = client['tmp']  # use a database called "state-store-models"
collection = db['tmp']

query = {"orderId": "1"}

results = collection.find(query)
for document in results:
    print(document)

document = {
    '_id': str(uuid.uuid4()),
    'value': json.dumps({}),
    '_etag': str(uuid.uuid4()),
    '_ttl': None
}

try:
    db['daprCollection'].insert_one(document)
except DuplicateKeyError:
    print(f'"{document["_id"]}" already exists in the store. Skipping...')