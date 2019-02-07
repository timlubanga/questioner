from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.helper import Helpers
from .utils.validator import Meetup_rsvpSchema
from flask_jwt_extended import jwt_required,get_jwt_identity




class RSVP(Resource):
	def __init__(self):
		self.meetup=Helpers()
		self.rsvp=Helpers()
		self.validate=Meetup_rsvpSchema()

	@jwt_required
	def post (self,_id):
		current_user=get_jwt_identity()
		data={
				"response":request.json["response"],
				"meetup_id":_id,
				"user_id":current_user
		}
		res=self.validate.load(data)
		if res.errors:
			return jsonify(res.errors)
	
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