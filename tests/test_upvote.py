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
		self.url_1="api/v1/question/upvote/javascript"
		self.url_2="api/v1/question/upvote/code fest"
		self.new_question={
							"CreatedBy":"john",
							"meetup_id":1,
							"body":"TDD best practices?"
							}

	def test_vote_increament(self):
		resp=self.app.patch(self.url_1)
		expected=json.loads(resp.get_data())
		
		self.assertEqual(resp.status_code,200)
		self.assertEqual(expected["data"]["upvotes"], 1)
	def test_downvoting_non_exisiting_question(self):
		resp=self.app.patch(self.url_2)
		expected=json.loads(resp.get_data())
		
		self.assertEqual(resp.status_code,404)
		self.assertEqual(expected["error"], "question does not exist")
	






if __name__ == '__main__':
	unittest.main()