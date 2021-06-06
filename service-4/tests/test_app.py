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
        response = self.client.post(url_for('get_fortune', day = "Friday(2022-06-03)", number = 20))
        self.assertEqual(response.data.decode(), "On Friday(2022-06-03) you will find nothing but peace & happiness")

