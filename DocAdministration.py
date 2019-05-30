#Document Administration - All combined
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/v1/AddDoc',methods=['PUT'])
def status():
    response = {'status' : 'Putting up a Doc'}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
