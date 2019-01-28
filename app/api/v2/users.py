
from flask import Flask,jsonify, make_response, request
import datetime
from .utils.helper import Helpers
from flask_restful import Resource, Api
from .utils.validator import  UserSchema

app = Flask(__name__)
api = Api(app)

class Users(Resource):
	def __init__(self):
		self.user=Helpers()
		self.validate=UserSchema()
	
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

		data=self.validate.load(params)
		if data.errors:
			return jsonify(data.errors)

		result=self.user.check_if_user_exists(params['username'])
		if result:
			return make_response(jsonify({"status":200,"message":"The user record exists"}),200)
		else:
			self.user.insert_new_user(params)
			return {
			"message":"user created successfully"
			}


	# retrieve all users from the user table
	def get(self):
		result=self.user.retriveve_all_users()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : result}),200)

		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "The user's table is empty"}),200)






