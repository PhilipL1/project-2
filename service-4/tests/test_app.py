from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app
from unittest.mock import patch 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_get_fortune(self):
        response = self.client.post(url_for('get_fortune', day = "Tuesday(2021-06-01)", number = 10))
        self.assertEqual(response.data.decode(), "On Tuesday(2021-06-01) you will find nothing but peace & happiness")





