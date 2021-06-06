from flask import Flask,request
import random
from os import getenv
import random 
import datetime 
import calendar

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

@app.route('/get_day',methods=['GET'])
def get_day():
    start_date = datetime.date(2022, 6, 1)
    end_date = datetime.date(2022, 7, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    date = str(random_date)
    #print(date)
    day = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    #print(day)
    answer_day = calendar.day_name[day]
    return_value =str(answer_day) + "("+str(date) + ")"
    return return_value

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

