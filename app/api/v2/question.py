from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.validator import QuestionSchema
from .utils.helper import check_if_ameetup_exist,check_if_a_question_exists,post_a_question
from flask_jwt_extended import jwt_required,get_jwt_identity

import datetime

app = Flask(__name__)
api = Api(app)

class Question(Resource):
	def __init__(self):
	   self.validate=QuestionSchema()

	@jwt_required
	def post(self,_id):
		current_user=get_jwt_identity()
		data={
					"createdon":datetime.datetime.now(),
					"createdby":current_user,
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
			result=check_if_ameetup_exist(_id)
			if result:
				post_a_question(data)
				return make_response(jsonify({
		   		"status" : 200,
		   		"message" : "question posted successfully"}),200)
			else:
		   		return make_response(jsonify({
		   		"status" : 200,
		   		"message" : "the meetup record does not exist"}),404)
		
	
	@jwt_required	  #get a specific question
	def get(self,_id):
		row=check_if_a_question_exists(_id)
		if row:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : row}),200)

		return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "The question record does not exist"}),200)
			
		

	




