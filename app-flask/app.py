import os
import random

from flask import Flask, jsonify
from faker import Faker
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

os.environ["FLASK_ENV"] = "development"

@app.route('/result', methods=['POST'])
def print_result():
    pass



@app.route('/data',methods=['GET'])
def get_data():
    fake = Faker()
    names = [fake.unique.name() for i in range(3000)]
    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8088)
