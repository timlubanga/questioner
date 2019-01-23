
from .user import User,api
from flask import jsonify, make_response, request
import datetime
from .utils.helper import Helpers
class Users(User):
	def __init__(self):
		self.user=Helpers()
	
	def post(self):
		params={
			"firstname":request.json["firstname"],
			"lastname":request.json["lastname"],
			"othername":request.json["othername"],
			"email":request.json["email"],
			"phone_number":request.json["phone_number"],
			"username":request.json["username"],
			"registered":datetime.datetime.now(),
			"password":request.json["password"],
			"isadmin":False
		}

		result=self.user.check_if_user_exists(params['username'])
		if result:
			return make_response(jsonify({"status":409,"error":"the record exists"}),409)
		else:
			self.user.insert_new_user(params)
			return {
			"message":"user created successfully"
			}


	# retrieve all users from the database
	def get(self):
		result=self.user.retriveve_all_users()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : result}),200)

		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "database is empty"}),200)






