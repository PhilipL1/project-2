from flask import Flask,request
import random
from os import getenv
import random 
import datetime 
import calendar

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

@app.route('/get_fortune/<day>/<int:number>', methods=['POST'])
def get_fortune(day, number):
    if number == 0:
        return f"On {day} you loose you're house and fiance, Sorry about that!"
    elif number <= 3 :
        return f"On {day}  you will win £300 from the lottery, that's it sorry!"
    elif number <= 6:
        return f"On {day} you will recieve unlimited food, Love dat!"
    elif number <= 9:
            return f"On {day} you will becomone a millionaire, lucky you!! "
    else :
        return f" On {day} you will find nothing but peace & happiness"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)