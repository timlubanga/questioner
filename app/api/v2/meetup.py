from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.validator import MeetupSchema
from .utils.helper import Helpers



app = Flask(__name__)
api = Api(app)


class Meetup(Resource):
	def __init__(self):
		self.validate=MeetupSchema()
		self.meetup=Helpers()
	
	def get(self,_id):
		row=self.meetup.check_if_ameetup_exist(_id)
		
		if row:
			return make_response(jsonify({
		   	"status" : 200,

		   	"data" : row}),200)

		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "record not found"}),404)

	def put(self,_id):
		data={
				"happeningOn":request.json["happeningOn"],
				"images":request.json["images"]
		}
		row=self.meetup.check_if_ameetup_exist(_id)
		if row:
			self.meetup.insert_new_meetup(data,_id)
		
			return make_response(jsonify({
			"status":404,
			"message" : "The meetup record updated successfully"}),200)
		
		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "The meetup record not found"}),404)


	
	def delete(self,_id):
		row=self.meetup.check_if_ameetup_exist(_id)
		if row:
			self.meetup.delete_ameetup_record(_id)
			return make_response(jsonify({
		   	"status":200,
		   	"message" : "record deleted successfully"}),200)
		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "record not found"}),404)

	



