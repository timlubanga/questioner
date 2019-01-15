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
		self.url="/api/v1/user/@timothy"
		self.url_1="/api/v1/user/@tim"
		self.new_user={
				"firstname":"timothy",
				"lastname":"lubanga",
				"othernames":"mutanyi",
				"email":"timlubanga@gmail.com",
				"phonenumber":"0714568338"
				}

	def test_register_new_user(self):
		response=self.app.post(self.url,data=json.dumps(self.new_user), headers={"Content-Type":"application/json"})
			
		expected=json.loads(response.get_data())
		self.assertEqual(response.status_code,201)
		self.assertEqual(len(expected["data"]),1)
		self.assertEqual(expected["data"][0]["username"],"@timothy")


			#test post exisitinng record
		resp=self.app.post(self.url,data=json.dumps(self.new_user), headers={"Content-Type":"application/json"})
		expe=json.loads(resp.get_data())
		self.assertEqual(resp.status_code,409)
		self.assertEqual(expe["error"], "the record exists")


	def test_retrieve_new_user(self):
		response=self.app.get(self.url)
		expected=json.loads(response.get_data())

		self.assertEqual(response.status_code,200)
		self.assertEqual(expected["data"][0]["username"],"@timothy")


	def test_retrieve_non_exsiting_user(self):
		
		response=self.app.get(self.url_1)
		expected=json.loads(response.get_data())
		self.assertEqual(response.status_code,200)
		self.assertEqual(expected["error"],"user does not exist")

	


if __name__ == '__main__':
	unittest.main()