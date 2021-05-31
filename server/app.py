from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
import requests 
from os import getenv
#from SQLAlchemy import desc


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Animals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #type = db.Column(db.String(50), nullable=False)
    fortune = db.Column(db.String(50), nullable=False)

@app.route('/')
def home():
    fortune = requests.get('http://fortune_api:5000/get_fortune')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)