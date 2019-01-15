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
		self.url="api/v1/question/TDD"

		self.new_question={
							"CreatedBy":"john",
							"meetup_id":1,
							"body":"TDD best practices?"
							}

	def test_post_anew_question(self):
		response=self.app.post(self.url,data=json.dumps(self.new_question), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,201)
		self.assertEqual(len(expected["data"]), 1)
		self.assertEqual(expected["data"][0]["title"],"TDD")	
		self.assertEqual(expected["data"][0]["body"],"TDD best practices?")	

	def test_post_duplicate_record(self):
		response=self.app.post(self.url,data=json.dumps(self.new_question), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,409)
		self.assertEqual(expected["error"],"the record already exists")

	def test_retrive_aspecific_question_record(self):
		response=self.app.get(self.url)
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,200)
		self.assertEqual(expected["data"][0]["body"],"TDD best practices?")
		
	def test_retrieve_non_excisting_record(self):
		url="api/v1/question/oop"
		response=self.app.get(url)
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,200)
		self.assertEqual(expected["error"],"record does not exist")


		

														






if __name__ == '__main__':
	unittest.main()