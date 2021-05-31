from flask import Flask,request
import random
from os import getenv
import random 
import datetime 
import calendar

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

# animal generator route here
@app.route('/get_random_generater',methods=['GET'])
def get_random_generater():
        return randint(0, 10)

@app.route('/get_day',methods=['GET'])
def get_day():
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        date = str(random_date)
        #print(date)
        day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
        #print(day)
        answer_day = calendar.day_name[day]
        return answer_day

@app.route('/get_fortune', methods=['POST'])
    def get_fortune(day, numbers):
        if numbers == 0:
            return f"On {day} you loose you're house and fiance, Sorry about that!"
        elif numbers <= 3 :
            return f"On {day}  you will in get £300, thats it sorry!"
        elif numbers <= 6:
            return f"On {day} you will recieve unlimited food, Love dat!"
        elif numbers <= 9:
             return f"On {day} you will becomone a millionaire "
        else :
            return f" On {day} you will find nothing but peace & happiness"

#date will determine if the fortune will become true or not 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)