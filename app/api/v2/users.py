
from flask import Flask,jsonify, make_response, request
import datetime
from .utils.helper import check_if_user_exists,retriveve_all_users,insert_new_user
from flask_restful import Resource, Api
from .utils.validator import  UserSchema
from flask_jwt_extended import jwt_required,get_jwt_identity

app = Flask(__name__)
api = Api(app)

class Users(Resource):
	def __init__(self):
		self.validate=UserSchema()
	
	def post(self):
		try:
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
		except Exception:
			return make_response(jsonify({
		   	"status" : 400,
		   	"error" : "missing required field in the body"
		   }),400)
		
		data=self.validate.load(params)
		if data.errors:
			return jsonify(data.errors)

		result=check_if_user_exists(params['username'])
		if result:
			return make_response(jsonify({"status":200,"message":"The user record exists"}),200)
		else:
			insert_new_user(params)
			return {
			"message":"user created successfully"
			}


	# retrieve all users from the user table
	@jwt_required
	def get(self):
		current_user=get_jwt_identity()
		if current_user!=1:
			return make_response(jsonify({
		   	"status" : 401,
		   	"message" : "you are not authorized to access this endpoint"}),401)

		result=retriveve_all_users()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : result}),200)

		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "The user's table is empty"}),200)






