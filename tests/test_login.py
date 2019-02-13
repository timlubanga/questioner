import unittest
import os
import sys
import json
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)

from app import create_app


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app=create_app().test_client()
        self.url="api/v2/login"
        self.data={
            "username":"@jossmeosee",
            "password": "@smart"
            }
        self.test_missing_password={
            "username":"@jossmeosee"
            }
        self.data1={
            "username":"@jossmeosee",
            "password": ""
            }
        self.data2={
            "username":"@jossmeosee",
            "password": "    "
            }
        self.data3={
            "username":"@jossmeosee",
            "password": "@eeeesmart"
            }

        self.data4={
            "username":"@joseeeesmeosee",
            "password": "@smart"
            }

        self.data5={
            "password": "@smart"
            }


    def test_successfully_login(self):
        response=self.app.post(self.url,data=json.dumps(self.data), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())

        self.assertEqual(expected["message"], "successfully logged in")
        self.assertEqual(response.status_code,200)

    def test_missing_password(self):
        response=self.app.post(self.url,data=json.dumps(self.test_missing_password), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())

        self.assertEqual(expected["error"], "missing username or password in the body")
        self.assertEqual(response.status_code, 400)

    def test_blank_password(self):
        response=self.app.post(self.url,data=json.dumps(self.data1), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())
        self.assertEqual(expected["error"]["password"][0], "Field cannot be blank and should be atleast 2 characters")

    def test_username_whitespace(self):
        response=self.app.post(self.url,data=json.dumps(self.data2), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())

        self.assertEqual(expected["error"]["password"][0], "no whitespaces")

    def test_wrong_password(self):
        response=self.app.post(self.url,data=json.dumps(self.data3), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())

        self.assertEqual(expected["message"], "wrong password")
    
    def test_non_exisiting_username(self):
    
        response=self.app.post(self.url,data=json.dumps(self.data4), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())
        self.assertEqual(expected["message"],"user does not exist")


    def test_missing_username(self):
        response=self.app.post(self.url,data=json.dumps(self.data5), headers={"Content-Type":"application/json"})
        expected=json.loads(response.get_data())

        self.assertEqual(expected["error"], "missing username or password in the body")




if __name__ == '__main__':
    unittest.main()