from flask_restful import Resource
from flask import Flask, jsonify, make_response, request
from .utils.validator import MeetupSchema
from .utils.helper import Helpers
from flask_jwt_extended import jwt_required,get_jwt_identity



class Meetup(Resource):
	def __init__(self):
		self.validate=MeetupSchema()
		self.meetup=Helpers()
	

	@jwt_required
	def get(self,_id):
		row=self.meetup.check_if_ameetup_exist(_id)
		
		if row:
			return make_response(jsonify({
		   	"status" : 200,

		   	"data" : row}),200)

		else:
			return make_response(jsonify({
		   	"status":200,
		   	"message" : "The meetup record is not found"}),200)

	@jwt_required
	def put(self,_id):
		data={
				"happeningon":request.json["happeningon"],
				"images":request.json["images"]
		}



		row=self.meetup.check_if_ameetup_exist(_id)
		if row:
			self.meetup.insert_new_meetup(data,_id)
		
			return make_response(jsonify({
			"status":202,
			"data":row,
			"message" : "The meetup record updated successfully"}),202)
		
		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "The meetup record not found"}),404)


	@jwt_required
	def delete(self,_id):
		row=self.meetup.check_if_ameetup_exist(_id)
		if row:
			self.meetup.delete_ameetup_record(_id)
			return make_response(jsonify({
		   	"status":200,
		   	"message" : "Record deleted successfully"}),200)
		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "The meetup record not found"}),404)

	



