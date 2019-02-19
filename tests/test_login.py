import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)

from app import create_app


class TestLogin(unittest.TestCase):
    def test_successfully_login(self):
        with create_app("testing").test_client() as client:
            self.url="api/v2/login"
            data_0={
            "username":"timo",
            "password": "tim@lubanga"
            }
            response=client.post(self.url,data=json.dumps(data_0), headers={"Content-Type":"application/json"})
            expected=json.loads(response.get_data())
            self.assertEqual(expected["message"], "successfully logged in")
    def test_missing_password(self):
        with create_app("testing").test_client() as client:
            self.url="api/v2/login"
            data_0={
            "username":"timo",
            "password": ""
            }
            response=client.post(self.url,data=json.dumps(data_0), headers={"Content-Type":"application/json"})
            expected=json.loads(response.get_data())
            self.assertEqual(expected["error"]["password"][0],"Field cannot be blank and should be atleast 2 characters")
    def test_missing_username(self):
        with create_app("testing").test_client() as client:
            self.url="api/v2/login"
            data_0={
            "password": "tim@lubanga"
            }
            response=client.post(self.url,data=json.dumps(data_0), headers={"Content-Type":"application/json"})
            expected=json.loads(response.get_data())
            self.assertEqual(expected["error"],"missing username or password in the body")
    def test_wrong_username(self):
        with create_app("testing").test_client() as client:
            self.url="api/v2/login"
            data_0={
            "username":"timothy",
            "password": "tim@lubanga"
            }
            response=client.post(self.url,data=json.dumps(data_0), headers={"Content-Type":"application/json"})
            expected=json.loads(response.get_data())
            self.assertEqual(expected["message"],"user does not exist")
    def test_wrong_password(self):
        with create_app("testing").test_client() as client:
            self.url="api/v2/login"
            data_0={
            "username":"timo",
            "password": "tim@lubanga1"
            }
            response=client.post(self.url,data=json.dumps(data_0), headers={"Content-Type":"application/json"})
            expected=json.loads(response.get_data())
            self.assertEqual(expected["message"],"wrong password")
    def test_missing_data_fields(self):
        with create_app("testing").test_client() as client:
            self.url="api/v2/login"
            data_0={
        
            }
            response=client.post(self.url,data=json.dumps(data_0), headers={"Content-Type":"application/json"})
            expected=json.loads(response.get_data())
            self.assertEqual(expected["error"],"missing username or password in the body")

if __name__ == '__main__':
    unittest.main()