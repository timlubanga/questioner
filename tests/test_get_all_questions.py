import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app

class TestMeetups(unittest.TestCase):

	def setUp(self):
		self.url="api/v1/questions"
		self.app=create_app().test_client()

	def test_get_all_meetups(self):
		response=self.app.get(self.url)
		expected=json.loads(response.get_data())
		self.assertEqual(response.status_code,200)
		self.assertEqual(expected["data"][0]["body"], "TDD best practices?")
		self.assertEqual(len(expected["data"]),1)

if __name__ == '__main__':
	unittest.main()