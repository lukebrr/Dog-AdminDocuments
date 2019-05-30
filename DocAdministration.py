#Document Administration - All combined

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/v1/Add',methods=['POST'])
def status():
    response = {'status' : 'Upload a Doc'}
    return jsonify(response)

@app.route('/api/v1/ChangeStatus',methods=['GET'])
def status():
    response = {'status' : 'Going from unprocessed to processed'}
    return jsonify(response)

@app.route('/api/v1/DeleteDocument',methods=['DELETE'])
def status():
    response = {'status' : 'Deleting a Doc'}
    return jsonify(response)

@app.route('/api/v1/SearchByStatus',methods=['GET'])
def status():
    response = {'status' : 'Find unprocessed docs'}
    return jsonify(response)

@app.route('/api/v1/SearchByHandlerID',methods=['GET'])
def status():
    response = {'status' : 'Find documents for certain handler'}
    return jsonify(response)

@app.route('/api/v1/SearchByDogID',methods=['GET'])
def status():
    response = {'status' : 'Find documents for certain dog'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
