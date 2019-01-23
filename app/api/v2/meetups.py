
from .meetup import api,Meetup
from flask import jsonify, make_response, request
import datetime
from .utils.helper import Helpers

class Meetups(Meetup):
	def __init__(self):
			self.meetup=Helpers()
	#post a meetup to meetups

	def post(self):
		data={
				"created_on":datetime.datetime.now(),
				"location":request.json["location"],
				"images":request.json["images"],
				"topic":request.json["topic"],
				"happeningOn":request.json["happeningOn"],
				"tags":request.json["tags"]
		}
		result=self.meetup.check_a_meetup_record_by_topic_name(data["topic"])
		if result:
			return make_response(jsonify(
				{"status":200,
				"message":"The meetup record exists"
				}
				),
			200)
		self.meetup.post_ameetup_record(data)
		return make_response(jsonify(
				{"status":200,
				"message":"The meetup record successfully posted"
				}
				),
				200)


	# retrieve all meetups from the database

	def get(self):
		result=self.meetup.get_all_meetups()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : result}),200)

		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "database is empty"}),200)






