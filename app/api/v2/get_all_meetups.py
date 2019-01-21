
from .meetup import Meetup,api
from flask import jsonify, make_response
from .models import meetups
class Meetups(Meetup):
	def get(self):
		if len(meetups)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "no record exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : meetups}),200)



