import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app

class Testsystem(unittest.TestCase):

	def setUp(self):
		self.app=create_app().test_client()
		self.url="/api/v1/meetup/code fest"
		self.new_meetup={
			"images":"images",
			"topic":"code fest",
			"location":"ihub",
			"HappeningOn":"12/1/2018",
			"Tags":"Tags"}
		self.new_rsvp={
		"user":1,
		"response":"yes"
		}
	

	def test_post_rsvp_successfully(self):
		url="/api/v1/meetups/code fest/rsvp"
		response=self.app.post(self.url,data=json.dumps(self.new_meetup), headers={"Content-Type":"application/json"})
		resp=self.app.post(url,data=json.dumps(self.new_rsvp), headers={"Content-Type":"application/json"})
		expected=json.loads(resp.get_data())

		self.assertEqual(resp.status_code,201)
		self.assertIsNotNone(expected["data"])
		self.assertEqual(expected["data"][0]["response"],"yes")
	def test_post_rspv_with_nonexisting_meetup(self):
		url="/api/v1/meetups/hackathon/rsvp"
		resp=self.app.post(url,data=json.dumps(self.new_rsvp), headers={"Content-Type":"application/json"})
		expected=json.loads(resp.get_data())

		self.assertEqual(resp.status_code,200)
		self.assertEqual(expected["error"],"the meetup does not exist")









if __name__ == '__main__':
	unittest.main()