import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app

class TestMeetup(unittest.TestCase):

	def setUp(self):
		self.app=create_app().test_client()
		self.url="api/v2/meetups"
		self.url_login="/api/v2/login"
		self.url_id="api/v2/meetup/2"
		self.url_id1="api/v2/meetup/3"
		
		self.user={
			"username":"timo",
			"password": "tim@lubanga"
			}

		self.new_meetup={
        	"images": "timothy.jpg",
        	"location": "kasarani",
        	"tags": "{tia,toa}",
        	"topic": "likanda",
        	"happeningon": "1/3/2019"
        		}

		self.new_meetup1={
        	"images": "timothy.jpg",
        	"location": "",
        	"tags": "{tia,toa}",
        	"topic": "likanda",
        	"happeningon": "1/3/2019"
        		}
		self.new_meetup2={
        	"images": "timothy.jpg",
        	"location": "kasarani",
        	"tags": "{tia,toa}",
        	"topic": "    ",
        	"happeningon": "1/3/2019"
        	}
	
		auth = self.app.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
		data=json.loads(auth.get_data())
		token=(data["token"])
		self.headers={}
		self.headers ["Content-Type"]= "application/json"
		self.headers['Authorization'] = 'Bearer {}'.format(token)

	def test_successfully_meetup_posting(self):
		
		response=self.app.post(self.url,data=json.dumps(self.new_meetup), headers=self.headers)
		expected=json.loads(response.get_data())
		print(expected)

	def test_authorized_meetup_posting(self):

		self.data={
			"username":"@jossmeosee",
			"password": "@smart"
			}

		auth = self.app.post(self.url_login, data=json.dumps(self.data), content_type='application/json')
		data=json.loads(auth.get_data())
		token=(data["token"])
		headers = {"Content-Type": "application/json"}
		headers['Authorization'] = 'Bearer {}'.format(token)

		response=self.app.post(self.url,data=json.dumps(self.data), headers=headers)
		expected=json.loads(response.get_data())
		

		self.assertEqual(response.status_code,401 )
		self.assertEqual(expected["message"],"you are not authorized to access this endpoint")

	def test_blank_fields(self):
		response=self.app.post(self.url,data=json.dumps(self.new_meetup1), headers=self.headers)
		expected=json.loads(response.get_data())
		
		self.assertEqual(expected["location"][0], "Field cannot be blank and should be atleast 2 characters")

	def test_whitespace_topic_field(self):
		response=self.app.post(self.url,data=json.dumps(self.new_meetup2), headers=self.headers)
		expected=json.loads(response.get_data())

		self.assertEqual(expected["topic"][0], "no whitespaces in this field")

	def test_retrieve_all_meetups(self):
		response=self.app.get(self.url, headers=self.headers)
		expected=json.loads(response.get_data())
		self.assertEqual(len(expected), 2)

	def test_retrieve_specific_meetup_record(self):
		response=self.app.get(self.url_id, headers=self.headers)
		expected=json.loads(response.get_data())
		
		self.assertEqual(expected["data"]["meetup_id"], 2)
		self.assertEqual(response.status_code,200)
		
	def test_retrieve_retrieve_nonexisiting_record(self):
		response=self.app.get(self.url_id1, headers=self.headers)
		expected=json.loads(response.get_data())

		self.assertEqual(expected["message"], "The meetup record is not found")

	def test_update_aspecific_record(self):
		data={
        	"images": "lubs.jpg",
        	"happeningon": "1/8/2019"
        	}
		response=self.app.put(self.url_id, data=json.dumps(data), headers=self.headers)
		expected=json.loads(response.get_data())

		self.assertEqual(expected["message"], "The meetup record updated successfully")
		self.assertEqual(expected["data"]["images"],"lubs.jpg")
		self.assertEqual(response.status_code,202)
















if __name__ == '__main__':
	unittest.main()