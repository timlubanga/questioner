from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import questions
from utils.validator import QuestionSchema

import datetime

app = Flask(__name__)
api = Api(app)

class Question(Resource):
	def __init__(self):
	   self.id = len(questions) + 1
	   self.validate=QuestionSchema()

	def post(self):
		new_question={
					"id":self.id,
					"CreatedOn":datetime.datetime.now(),
					"CreatedBy":request.json["CreatedBy"],
					"meetup_id":request.json["meetup_id"],
					"title":request.json["title"],
					"body":request.json["body"],
					"upvotes":0,
					"downvotes":0
					}
		result=self.validate.load(new_question)
		if result.errors:
			return jsonify(result.errors)
		question=[question for question in questions if question["id"]==request.json["id"]]
		if len(question)==0:
			questions.append(new_question)
			return make_response(jsonify({
		   	"status" : 201,
		   	"data" : questions}),201)
		else:
			return make_response(jsonify({
		   	"status" : 409,
		   	"error" : "the record already exists"}),409)
		  
		  #get a specific question
	def get(self):
		question_id=request.json["id"]
		question=[question for question in questions if question["id"]==question_id]
		if len(question)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : question}),200)
		

	




