from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.validator import QuestionSchema
from .utils.helper import Helpers

import datetime

app = Flask(__name__)
api = Api(app)

class Question(Resource):
	def __init__(self):
	   self.validate=QuestionSchema()
	   self.question=Helpers()
	   self.meetup=Helpers()


	def post(self,_id):
		data={
					"createdon":datetime.datetime.now(),
					"createdby":request.json["createdby"],
					"meetup_id":_id,
					"title":request.json["title"],
					"body":request.json["body"],
					"upvotes":0,
					"downvotes":0
					}
		result=self.validate.load(data)
		if result.errors:
			return jsonify(result.errors)
		else:
			result=self.meetup.check_if_ameetup_exist(_id)
			if result:
				self.question.post_a_question(data)
				return make_response(jsonify({
		   		"status" : 200,
		   		"message" : "question posted successfully"}),200)
		   	else:
		   		return make_response(jsonify({
		   		"status" : 200,
		   		"message" : "the meetup record does not exist"}),404)
		
		  #get a specific question
	def get(self,_id):
		row=self.question.check_if_a_question_exists(_id)
		if row:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : row}),200)

		return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "The question record does not exist"}),200)
			
		

	




