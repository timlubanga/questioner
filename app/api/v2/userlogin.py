
from flask_restful import Resource,reqparse,Api
from flask import Flask
from .utils.helper import Helpers
from .utils.validator import Login
from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import (create_access_token, JWTManager,get_jwt_identity)
from  marshmallow import ValidationError
import json


class Userlogin(Resource):

	def __init__(self):
		self.user=Helpers()
		self.validate=Login()


	def post(self):
		try:
			data={ 
				"username":request.json["username"],
				"password":request.json["password"]

			}
		except Exception:
			return make_response(jsonify({
		   	"status" : 400,
		   	"error" : "missing username or password in the body"
		   }),400)
		
		result=self.validate.load(data)
		if result.errors:
			return {"error":result.errors}
		user=self.user.check_if_user_exists(data['username'])

		if not user:
			return {"message":"user does not exist"}

		if data['password'] == user['password']:
			access_token = create_access_token(identity = user['id'])
	
			return make_response(jsonify({
		   	"status" : 200,
		   	"message":"successfully logged in",
		   	"token" : access_token
		   }),200)
		else:
			return{"message":"wrong password"}

      

		
