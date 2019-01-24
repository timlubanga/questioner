from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.validator import UserSchema
from .utils.helper import Helpers
from flask_jwt_extended import jwt_required

app = Flask(__name__)
api = Api(app)


class User(Resource):
	def __init__(self): 
	   self.validate=UserSchema()
	   self.user=Helpers()
	

		# GET a user with a spefic username
	@jwt_required
	def get(self,username):
		row=self.user.check_if_user_exists(username)
		if row:
			return make_response(jsonify({
		   	"status" : 200,

		   	"data" : row}),200)

		else:
			return make_response(jsonify({
		   	"status":200,
		   	"message" : "The user record not found"}),200)
	

