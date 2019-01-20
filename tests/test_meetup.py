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
		self.url="/api/v1/meetup"
		self.new_meetup={
			"images":"images",
			"topic":"code fest",
			"location":"ihub",
			"HappeningOn":"12/1/2018",
			"Tags":"Tags"}
		self.new_meetup_1={
			"images":"images",
			"topic":"hackathon",
			"location":"ihub",
			"HappeningOn":"12/1/2018",
			"Tags":"Tags"
			}

	def test_post_anew_meetup_record(self):
		
		response=self.app.post(self.url,data=json.dumps(self.new_meetup), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code, 201)
		self.assertEqual(len(expected["data"]),1)
	def test_retrieve_ameetup_record(self):
		
		response=self.app.get(self.url,data=json.dumps(self.new_meetup), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,200)
		print(expected)
		self.assertEqual(expected["data"]["HappeningOn"],"12/1/2018")

	def test_post_duplicate_meetup_record(self):

		response=self.app.post(self.url,data=json.dumps(self.new_meetup), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())
		self.assertEqual(expected["error"],"the record already exists")
		self.assertEqual(response.status_code,409)

	def test_retreive_non_exisiting_meetup_record(self):
		url="/api/v1/meetup"
		response=self.app.get(self.url,data=json.dumps(self.new_meetup_1), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,200)
		self.assertEqual(expected["error"], "record does not exist")

	def test_updating_new_record(self):

		new_meetup={
			"id":1,
			"HappeningOn":"12/1/2019",
			"Tags":"tag1"
			}
		response=self.app.put(self.url,data=json.dumps(new_meetup), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,202)
		self.assertEqual(expected["data"][0]["HappeningOn"],"12/1/2019")
		self.assertEqual(expected["data"][0]["Tags"],"tag1")
	
			





if __name__ == '__main__':
	unittest.main()