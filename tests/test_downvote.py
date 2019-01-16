import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app

class Testdownvote(unittest.TestCase):

	def setUp(self):
		self.app=create_app().test_client()
		self.url="api/v1/question/javascript"
		self.url_1="api/v1/question/downvote/javascript"
		self.url_2="api/v1/question/downvote/code fest"
		self.new_question={
							"CreatedBy":"john",
							"meetup_id":1,
							"body":"TDD best practices?"
							}

	def test_vote_decrement(self):
		response=self.app.post(self.url,data=json.dumps(self.new_question), headers={"Content-Type":"application/json"})
		resp=self.app.patch(self.url_1)
		expected=json.loads(resp.get_data())
		
		self.assertEqual(resp.status_code,200)
		self.assertEqual(expected["data"]["downvotes"], -1)
	def test_downvoting_non_exisiting_question(self):
		response=self.app.post(self.url,data=json.dumps(self.new_question), headers={"Content-Type":"application/json"})
		resp=self.app.patch(self.url_2)
		expected=json.loads(resp.get_data())
		
		self.assertEqual(resp.status_code,404)
		self.assertEqual(expected["error"], "question does not exist")
	def test_downvoting_empty_database(self):

		resp=self.app.patch(self.url_2)
		expected=json.loads(resp.get_data())

		self.assertEqual(resp.status_code,404)
		self.assertEqual(expected["error"],"the database is empty, no records available")





if __name__ == '__main__':
	unittest.main()