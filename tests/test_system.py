import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app

class Testsystem(unittest.TestCase):

	def test_register_new_user(self):
		url="/api/v1/@timothy"
		with create_app().test_client() as c:
			new_user={
				"firstname":"timothy",
				"lastname":"lubanga",
				"othernames":"mutanyi",
				"email":"timlubanga@gmail.com",
				"phonenumber":"0714568338",
				"username":"@timothy"
		}
			response=c.post(url,data=json.dumps(new_user), headers={"Content-Type":"application/json"})
			
			
			expected=json.loads(response.get_data())
			self.assertEqual(response.status_code,201)
			self.assertEqual(len(expected["data"]),1)
			self.assertEqual(expected["data"][0]["username"],"@timothy")



			resp=c.post(url,data=json.dumps(new_user), headers={"Content-Type":"application/json"})
			expe=json.loads(resp.get_data())
			self.assertEqual(resp.status_code,409)
			self.assertEqual(expe["error"], "the record exists")


	def test_retrieve_new_user(self):
		with create_app().test_client() as c:
			url="/api/v1/@timothy"
			response=c.get(url)
			expected=json.loads(response.get_data())

			self.assertEqual(response.status_code,200)
			self.assertEqual(expected["data"][0]["username"],"@timothy")


	def test_retrieve_non_exsiting_user(self):
		with create_app().test_client() as c:
			url="/api/v1/@tim"
			response=c.get(url)
			expected=json.loads(response.get_data())
			self.assertEqual(response.status_code,200)
			self.assertEqual(expected["error"],"the user does not exist")

	def test_post_anew_meetup_record(self):
		with create_app().test_client() as c:
			url="/api/v1/meetup/code fest"
			new_meetup={
			"images":"images",
			"topic":"code fest",
			"HappeningOn":"12/1/2018",
			"Tages":"Tages"}
			response=c.post(url,data=json.dumps(new_meetup), headers={"Content-Type":"application/json"})
			expected=json.loads(response.get_data())

			self.assertEqual(response.status_code, 201)
			self.assertEqual(len(expected["data"]),1)

	def test_post_duplicate_meetup_record(self):
		pass

	def test_incorrect_meetup_record(self):
		pass

	def test_retrieve_ameetup_record(self):
		pass

	def test_retreive_non_exisiting_meetup_record(self):
		pass

if __name__ == '__main__':
	unittest.main()