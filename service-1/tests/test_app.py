from flask import url_for 
from flask_testing import TestCase
import requests_mock 
from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db"
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        
class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker: 
            mocker.get('http://number_api:5000/get_number', json = {'number': 9})
            mocker.get('http://day_api:5000/get_day', text = 'Thursday(2021-06-03)')
            mocker.post('http://fortune_api:5000/get_fortune/Thursday(2021-06-03)/9', text = 'On Thursday(2021-06-03) you will becomone a millionaire, lucky you!!')
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'On Thursday(2021-06-03) you will becomone a millionaire, lucky you!!', response.data)


