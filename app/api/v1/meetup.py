from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import meetups
from .utils.validator import MeetupSchema

import datetime

app = Flask(__name__)
api = Api(app)


class Meetup(Resource):
	def __init__(self):
	   self.id = len(meetups) + 1
	   self.validate=MeetupSchema()

	def post(self):
		new_meetup={
					"id":self.id,
					"CreatedOn":datetime.datetime.now(),
					"location":request.json["location"],
					"images":request.json["images"],
					"topic":request.json["topic"],
					"HappeningOn":request.json["HappeningOn"],
					"Tags":request.json["Tags"]
					}
		result=self.validate.load(new_meetup)
		if result.errors:
			return jsonify(result.errors)

		meetup=[meetup for meetup in meetups if meetup["topic"]==request.json["topic"]]
		if len(meetup)==0:
			meetups.append(new_meetup)
			return make_response(jsonify({
		   	"status" : 201,
		   	"data" : meetups}),201)
		else:
			return make_response(jsonify({
		   	"status" : 409,
		   	"error" : "the record already exists"}),409)
		   	#get a specific meetup record
	def get(self):
		topic_name=request.json["topic"]
		meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		if len(meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : meetup[0]}),200)

	def put(self):
		record_id=request.json["id"]
		new_meetup=[meetup for meetup in meetups if meetup["id"]==record_id]
		if len(new_meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		new_meetup[0]["HappeningOn"]=request.json["HappeningOn"]
		new_meetup[0]["Tags"]=request.json["Tags"]
		return make_response(jsonify({"status":202,"data":meetups}), 202)

	def delete(self):
		topic_id=request.json["id"]
		meetup=[meetup for meetup in meetups if meetup["id"]==topic_id]
		if len(meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		meetups.remove(meetup[0])
		return make_response(jsonify({"status":200,"data":meetups}), 200)  






