import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app


class Testsignup(unittest.TestCase):

	def setUp(self):
		self.app=create_app().test_client()
		self.data_0={
			"firstname":"johng",
			"lastname":"james",
			"othername":"kevoh",
			"email":"jofns2ss@gmail.com",
			"phone_number":"0714567894",
			"username":"@jossmeosee",
			"password": "@smart"
			}
		self.data={
			"firstname":"johng",
			"lastname":"james",
			"othername":"kevoh123",
			"email":"jofns2ss@gmail.com",
			"phone_number":"0714567894",
			"username":"@jossmeosee",
			"password": "@smart"
			}

		self.data1={
			"lastname":"james",
			"othername":"kevoh",
			"email":"jofns2ss@gmail.com",
			"phone_number":"0714567894",
			"username":"@jossmeosee",
			"password": "@smart"
			}

		self.data2={
			"firstname":"johng",
			"lastname":"james",
			"othername":"kevoh",
			"email":"jofns2ss@gmail.com",
			"phone_number":"0714567894r",
			"username":"@jossmeosee",
			"password": "@smart"
			}

		self.data3={
			"firstname":"johng",
			"lastname":"james",
			"othername":"kevoh",
			"email":"jofns",
			"phone_number":"0714567894",
			"username":"@jossmeosee",
			"password": "@smart"
			}
		self.url="api/v2/users"
	def test_missing_firstname(self):
		response=self.app.post(self.url,data=json.dumps(self.data1), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())
		self.assertEqual(expected["error"], "missing required field in the body")
		self.assertEqual(response.status_code,400)


	def test_successful_sign_up(self):
		response=self.app.post(self.url,data=json.dumps(self.data), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())
		
		self.assertEqual(response.status_code,200)
		self.assertEqual(expected['othername'][0],'the characters should be digits only')

	def test_wrong_phone_number(self):
		response=self.app.post(self.url,data=json.dumps(self.data2), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())
		self.assertEqual(expected["phone_number"][0], "the characters should be digits only")
		self.assertEqual(response.status_code,200)

	def test_wrong_wrong_email_format(self):
		response=self.app.post(self.url,data=json.dumps(self.data3), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())
		self.assertEqual(expected["email"][0], "Not a valid email address.")
		self.assertEqual(response.status_code,200)

	def test_duplicate_data_record(self):
		response=self.app.post(self.url,data=json.dumps(self.data_0), headers={"Content-Type":"application/json"})
		expected=json.loads(response.get_data())
		self.assertEqual(expected["message"],"The user record exists")











if __name__ == '__main__':
	unittest.main()