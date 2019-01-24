from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.helper import Helpers




class RSVP(Resource):
	def __init__(self):
		self.meetup=Helpers()
		self.rsvp=Helpers()

	def post (self,_id):
		data={
				"response":request.json["response"],
				"meetup_id":_id,
				"user_id":request.json["user_id"]
		}
		result=self.meetup.check_if_ameetup_exist(_id)

		if result:
			self.rsvp.post_rsvp(data)

			return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "Thank you, your response recorded successfully"}),200)
		else:
			return make_response(jsonify({
		   		"status" : 200,
		   		"message" : "The meetup record does not exist"}),200)