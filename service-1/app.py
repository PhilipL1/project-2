from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
import requests 
from os import getenv
#from SQLAlchemy import desc


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Fortunes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fortune = db.Column(db.String(1000), nullable=False)

@app.route('/')
@app.route("/home")
def home():
    number = requests.get('http://number-api:5000/get_number').json()['number']
    day = requests.get('http://day-api:5000/get_day')
    fortune = requests.post(f'http://fortune-api:5000/get_fortune/{day.text}/{number}')


    
    db.session.add(
        Fortunes(
            fortune = fortune.text
        )
    )
    db.session.commit()
    last_three_fortune = Fortunes.query.order_by(Fortunes.id.desc()).limit(3).all()

    return render_template("home.html", title="Home", number=number,\
    day=day.text, fortune=fortune.text, all_fortune = last_three_fortune)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)