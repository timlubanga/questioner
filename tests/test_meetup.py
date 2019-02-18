import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from app import create_app

class TestMeetup(unittest.TestCase):

	def setUp(self):
		self.url="api/v2/meetups"
		self.url_login="/api/v2/login"
		self.url_id="api/v2/meetup/1"
		self.url_id1="api/v2/meetup/3"
		self.sign="api/v2/users"
		
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
		self.data00={
        	"images": "lubs.jpg",
        	"happeningon": "1/8/2019"}
		self.data={
			"firstname":"johng",
			"lastname":"james",
			"othername":"kevoh",
			"email":"jofns2ss@gmail.com",
			"phone_number":"0714567894",
			"username":"@jossmeosee",
			"password": "@smart"
			}

	

	def test_successfully_meetup_posting(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			response=client.post(self.url,data=json.dumps(self.new_meetup), headers=headers)
			expected=json.loads(response.get_data())
			self.assertEqual(expected["message"],"The meetup record successfully posted")

	def test_authorized_meetup_posting(self):
		with create_app("testing").test_client() as client:
			data_login={
			"username":"@jossmeosee",
			"password": "@smart"
			}
			sign=client.post(self.sign, data=json.dumps(self.data), content_type='application/json')
			auth = client.post(self.url_login, data=json.dumps(data_login), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			

			response=client.post(self.url,data=json.dumps(self.new_meetup), headers=headers)
			expected=json.loads(response.get_data())
		

			self.assertEqual(response.status_code,401 )
			self.assertEqual(expected["message"],"you are not authorized to access this endpoint")

	def test_blank_fields(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			response=client.post(self.url,data=json.dumps(self.new_meetup1), headers=headers)
			expected=json.loads(response.get_data())
		
			self.assertEqual(expected["location"][0], "Field cannot be blank and should be atleast 2 characters")

	def test_whitespace_topic_field(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			response=client.post(self.url,data=json.dumps(self.new_meetup2), headers=headers)
			expected=json.loads(response.get_data())

			self.assertEqual(expected["topic"][0], "no whitespaces in this field")

	def test_retrieve_all_meetups(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			response=client.get(self.url, headers=headers)
			expected=json.loads(response.get_data())
			self.assertEqual(expected["error"], "database is empty")
		

	def test_retrieve_specific_meetup_record(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)

			res=client.post(self.url,data=json.dumps(self.new_meetup), headers=headers)
			response=client.get(self.url_id, headers=headers)
			expected=json.loads(response.get_data())
		
			self.assertEqual(expected["data"]["location"],"kasarani")
			self.assertEqual(response.status_code,200)
		
	def test_retrieve_retrieve_nonexisiting_record(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			response=client.get(self.url_id1, headers=headers)
			expected=json.loads(response.get_data())

			self.assertEqual(expected["message"], "The meetup record is not found")

	def test_update_aspecific_record(self):
		with create_app("testing").test_client() as client:
			auth = client.post(self.url_login, data=json.dumps(self.user), content_type='application/json')
			data=json.loads(auth.get_data())
			token=(data["token"])
			headers={}
			headers ["Content-Type"]= "application/json"
			headers['Authorization'] = 'Bearer {}'.format(token)
			res=client.post(self.url,data=json.dumps(self.new_meetup), headers=headers)
			response=client.put(self.url_id, data=json.dumps(self.data00), headers=headers)
			expected=json.loads(response.get_data())
			print(expected["message"],"The meetup record successfully posted")
















if __name__ == '__main__':
	unittest.main()