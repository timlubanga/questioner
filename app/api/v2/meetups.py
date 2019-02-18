
from .meetup import Meetup
from flask import jsonify, make_response, request
import datetime
from .utils.helper import check_a_meetup_record_by_topic_name, post_ameetup_record,get_all_meetups
from .utils.validator import MeetupSchema
from flask_jwt_extended import jwt_required,get_jwt_identity

class Meetups(Meetup):
	def __init__(self):
		self.validate=MeetupSchema()
	#post a meetup to meetups
	@jwt_required
	def post(self):
		current_user=get_jwt_identity()
		if current_user!=1:
			return make_response(jsonify({
		   	"status" : 401,
		   	"message" : "you are not authorized to access this endpoint"}),401)
		payload={
				"created_on":datetime.datetime.now(),
				"location":request.json["location"],
				"images":request.json["images"],
				"topic":request.json["topic"],
				"happeningon":request.json["happeningon"],
				"tags":request.json["tags"]
		}

		res=self.validate.load(payload)
		if res.errors:
			return jsonify(res.errors)
		result=check_a_meetup_record_by_topic_name(payload["topic"])
		if result:
			return make_response(jsonify(
				{"status":200,
				"message":"The meetup record exists"
				}
				),
			200)
		post_ameetup_record(payload)
		return make_response(jsonify(
				{"status":200,
				"message":"The meetup record successfully posted"
				}
				),
				200)


	# retrieve all meetups from the database
	@jwt_required
	def get(self):
		result=get_all_meetups()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : result}),200)

		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "database is empty"}),200)






