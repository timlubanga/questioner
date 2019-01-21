
from .user import User,api
from flask import jsonify, make_response
from .models import users
class Users(User):
	def get(self):
		if len(users)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "no record exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : users}),200)



