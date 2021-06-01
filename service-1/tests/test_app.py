from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from service-1 import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home():
        with request_mock.Mocker() as mocker: 
            mocker.get('http://number_api:5000/get_number', text = '9')
            mocker.get('http://day_api:5000/get_day', text = 'Monday')
            mocker.post('http://fortune_api:5000/get_fortune', text = "On Monday you will becomone a millionaire ")
        response = self.client.get(url_for('home'))
        self.asserEqual(response.status_code, 200)


