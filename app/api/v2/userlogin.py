
from flask_restful import Resource,reqparse,Api
from flask import Flask
from .utils.helper import Helpers
from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import (create_access_token, JWTManager,get_jwt_identity)

app = Flask(__name__)
api = Api(app)
# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'timothy'  
jwt = JWTManager(app)



parser = reqparse.RequestParser()
parser.add_argument('username', help = 'This field cannot be blank', required = True)
parser.add_argument('password', help = 'This field cannot be blank', required = True)


class Userlogin(Resource):

	def __init__(self):
		self.user=Helpers()

	def post(self):
		data = parser.parse_args()
		user=self.user.check_if_user_exists(data['username'])

		if not user:
			return {'user does not exist'}

		if data['password'] == user['password']:
			access_token = create_access_token(identity = user['id'])
			return make_response(jsonify({
		   	"status" : 200,
		   	"token" : access_token,
		   	"message" : "loggged in"}),200)

      

		
