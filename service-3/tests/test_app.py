from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app
import re

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_day(self):
        for _ in range(20):
            response = self.client.get(url_for('get_day'))
            day,year,month,date = re.findall("(\S+)\((\d{4})-(\d{2})-(\d{2})\)", response.data.decode())[0]
            self.assertIn(day, {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"})
            self.assertEqual(year, "2022")
            self.assertIn(month,{"06", "07"})
            self.assertIn(int(date), range(0, 31))


            


