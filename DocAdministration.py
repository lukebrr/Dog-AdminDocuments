#Document Administration - All combined

from flask import Flask, jsonify, request
import os
from pymongo import MongoClient
import pymongo

print "\n## Establish the connection and aim at a specific database"
client = MongoClient('127.0.0.1:27017')
db = client.dogdocs
print db

app = Flask(__name__)

@app.route('/api/v1/add',methods=['POST'])
def add():
    response = {'status' : 'Upload a Doc'}
    data = request.form
    s3id = data['s3id']
    handlerid = data['handlerid']
    dogid = data['dogid']
    status = data['status']
    vacc1 = data['vacc1']
    vacc2 = data['vacc2']
    vacc3 = data['vacc3']
    vacc4 = data['vacc4']
    res = db.docs.insert_one({"s3id" : s3id,
                              "handlerid" : handlerid,
                              "dogid" : dogid,
                              "status" : status})
    #if res =
    #res = db.docs.insert_one({'s3id' : s3id})
    print res
    return jsonify(response)

@app.route('/api/v1/changestatus',methods=['GET'])
def changestatus():
    response = {'status' : 'Going from unprocessed to processed'}
    return jsonify(response)

@app.route('/api/v1/deletedocument',methods=['DELETE'])
def deldocument():
    response = {'status' : 'Deleting a Doc'}
    return jsonify(response)

@app.route('/api/v1/searchbystatus',methods=['GET'])
def searchstatus():
    req = request.args
    status = req["status"]
    cursor = db.docs.find({"status": status})
    matches = []
    for everydoc in cursor:
        matches.append({"s3id": everydoc["s3id"],
                        "handlerid": everydoc["handlerid"],
                        "dogid": everydoc["dogid"],
                        "status": everydoc["status"],
                        "vacc1" = everydoc['vacc1'],
                        "vacc2" = everydoc['vacc2'],
                        "vacc3" = everydoc['vacc3'],
                        "vacc4" = everydoc['vacc4']})
    response = {"documents": matches} 
    return jsonify(response)

@app.route('/api/v1/searchbyhandlerid',methods=['GET'])
def searchhandler():
    req = request.args
    handler = req["handlerid"]
    cursor = db.docs.find({"handlerid": handlerid})
    matches = []
    for everydoc in cursor:
        matches.append({"s3id": everydoc["s3id"],
                        "handlerid": everydoc["handlerid"],
                        "dogid": everydoc["dogid"],
                        "status": everydoc["status"],
                        "vacc1" = everydoc['vacc1'],
                        "vacc2" = everydoc['vacc2'],
                        "vacc3" = everydoc['vacc3'],
                        "vacc4" = everydoc['vacc4']})
    response = {"documents": matches}
    return jsonify(response)

@app.route('/api/v1/searchbydogid',methods=['GET'])
def searchdog():
    req = request.args
    dog = req["dogid"]
    cursor = db.docs.find({"dogid": dogid})
    matches = []
    for everydoc in cursor:
        matches.append({"s3id": everydoc["s3id"],
                        "handlerid": everydoc["handlerid"],
                        "dogid": everydoc["dogid"],
                        "status": everydoc["status"],
                        "vacc1" = everydoc['vacc1'],
                        "vacc2" = everydoc['vacc2'],
                        "vacc3" = everydoc['vacc3'],
                        "vacc4" = everydoc['vacc4']})
    response = {"documents": matches}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
