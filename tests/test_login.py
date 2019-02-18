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
            print(expected)
if __name__ == '__main__':
    unittest.main()