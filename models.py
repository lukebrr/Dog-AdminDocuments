#!/usr/bin/env python

#########################################################
# This is the functional processing file.
# It contains the DB connections, queries and processes
#########################################################

# Import modules required for app
import os, time, json, re
from pymongo import MongoClient
from bson.objectid import ObjectId

def db_conn():
    # Check if user defined environment variable exists
    if "DB_URI" in os.environ:
        DB_ENDPOINT = MongoClient(os.environ['DB_URI'])
        DB_NAME = os.environ['DB_Name']

    # Check if running in Pivotal Web Services with MongoDB service bound
    elif 'VCAP_SERVICES' in os.environ:
        VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
        MONGOCRED = VCAP_SERVICES["mlab"][0]["credentials"]
        DB_ENDPOINT = MongoClient(MONGOCRED["uri"])
        DB_NAME = str(MONGOCRED["uri"].split("/")[-1])

    # Otherwise, assume running locally with local MongoDB instance
    else:
##	    DB_ENDPOINT = MongoClient('127.0.0.1:27017')
	    DB_ENDPOINT = MongoClient('192.168.26.130:27017')
	    DB_NAME = "DocoAdmin"
    # Get database connection using database endpoint and name defined above
    global db
    db = DB_ENDPOINT[DB_NAME]

def init_db():
    db_conn() # Connect to database

# [C]rud: Add a new document entry, return the document id
def new_doco(doco):
    
    # If document id already exists in the system then raise an error
##    doco_exists = db.doco_details.find_one({'id': doco['id']})

##    if not doco_exists:
        # Add doco to database
##        _id = db.doco_details.insert_one({'doc_id': doco['doc_id'],
    _id = db.doco_details.insert_one({'doco_type': doco['doco_type'],
                                    'name': doco['name'],
                                    'status': doco['status'],
                                    'handler_id': doco['handler_id'],
                                    'dog_id': doco['dog_id'] })
                                    
    return str(_id.inserted_id)

# c[R]ud: Retrieve a doocument by id
def get_doco(doco_id):
    doco_rec = db.doco_details.find_one({'_id': ObjectId(doco_id)})
    # Check if document exists
    if doco_rec:
        doco = {
            'id': doco_id,
            'doco_type': doco_rec.get('doco_type'),
            'name':doco_rec.get('name'),
            'status': doco_rec.get('status'),
            'handler_id': doco_rec.get('handler_id'),
            'dog_id': doco_rec.get('dog_id'),
        }
        return doco
    else:
        return None

# Return an array of document details, limited by max_number
def get_documents(max_number = 10):
    documents = []

    for doc in db.doco_details.find().sort("name", 1).limit(max_number):
        doco = {
            'id': str(doc.get('_id')),
            'doco_type': doc.get('doco_type'),
            'name': doc.get('name'),
            'status': doc.get('status'),
            'handler_id': doc.get('handler_id'),
            'dog_id': doc.get('dog_id')
        }
        documents.append(doc)

    return documents

# cr[U]d: Update a document record
def update_doco(doco):
    # Update document fields if present
    db.doco_details.update_one({'_id': ObjectId(doco['id'])},
                    { "$set" :{ 'handler_id': doco['handler_id'],
##                                'dog_id': doco['dog_id'],
##                                'doco_type': doco['doco_type'],
##                                'name': doco['name'],
                                'status': doco['status'],
                                }
                    },
                    upsert=True)
    return

### cru[D]: Delete a document by id , won't happen, we're not deleting anything
##def delete_doco(doc_id):
##    db.doco_details.delete_one({'_id': ObjectId(doc_id)})

# Retrieve a document by id
def get_document(doco_id):
    doc = db.doco_details.find_one({'_id': ObjectId(doco_id)})
    # Check if document exists
    if doc:
        doco = {
            'id': str(doc.get('_id')),
            'doco_type': doc.get('doco_type'),
            'name': doc.get('name'),
            'status': doc.get('status'),
            'handler_id': doc.get('handler_id'),
            'dog_id': doc.get('dog_id') 
        }
        return doc
    else:
        return None

# Generic search by criteria (dictionary of fields)
def search(criteria):
    documents = []

    for doc in db.doco_details.find(criteria):
        doco = {
            'id': str(doc.get('_id')),
            'doco_type': doc.get('doco_type'),
            'name': doc.get('name'),
            'status': doc.get('status'),
            'handler_id': doc.get('handler_id'),
            'dog_id': doc.get('dog_id')   
        }
        documents.append(doco)
    
    return documents
