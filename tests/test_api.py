import unittest
import requests
from model import Link
from main import connect


class ApiTest(unittest.TestCase):

    def test_hash_created(self):
        url = 'http://127.0.0.1:5000/shorten'
        data = {
            "url": "http://v1.windows93.net/",
            "expiredDate": "90"
        }
        response = requests.post(url, json=data)
        case_data = response.json()
        self.assertIn("hash", case_data)

    def test_link_redirect(self):
        url = 'http://127.0.0.1:5000/shorten'
        data = {
            "url": "https://cat-bounce.com/",
            "expiredDate": "365"
        }
        response = requests.post(url, json=data)
        case_data = response.json()
        hash_url = case_data["hash"]
        link = Link.objects(hash=hash_url).first()
        self.assertEqual(link.url, data["url"])

    def test_link_empty(self):
        url = 'http://127.0.0.1:5000/shorten'
        data = {
            "url": "",
            "expiredDate": "365"
        }
        response = requests.post(url, json=data)
        case_data = response.json()
        req_result = case_data["success"]
        self.assertEqual(req_result, 'false')

        

