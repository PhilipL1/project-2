from flask import Flask,request, jsonify
import random
from os import getenv
import random 


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

# animal generator route here
@app.route('/get_number',methods=['GET'])
def get_number():
    result = {'number':random.randint(0, 10)}
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)