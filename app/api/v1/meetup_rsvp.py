from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import meetups
from .models import rsvps



class RSVP(Resource):
	def __init__(self):
		self.id=len(rsvps)

	def post (self,topic_name):
		meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		if len(meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "the meetup does not exist"}),200)
		else:
			new_rsvp={
					"id":self.id,
					"meetup_id":meetup[0]["id"],
					"user":request.json["user"],
					"response":request.json["response"]
					}

			rsvps.append(new_rsvp)
			return make_response(jsonify({
		   		"status" : 201,
		   		"data" : rsvps}),201)