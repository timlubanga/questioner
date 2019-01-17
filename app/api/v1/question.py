from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import questions

import datetime

app = Flask(__name__)
api = Api(app)

class Question(Resource):
	def __init__(self):
	   self.id = len(questions) + 1

	def post(self,title_name):
		question=[question for question in questions if question["title"]==title_name]
		if len(question)==0:
			new_question={
					"id":self.id,
					"CreatedOn":datetime.datetime.now(),
					"CreatedBy":request.json["CreatedBy"],
					"meetup_id":request.json["meetup_id"],
					"title":title_name,
					"body":request.json["body"],
					"upvotes":0,
					"downvotes":0
					}
			questions.append(new_question)
			return make_response(jsonify({
		   	"status" : 201,
		   	"data" : questions}),201)
		else:
			return make_response(jsonify({
		   	"status" : 409,
		   	"error" : "the record already exists"}),409)
		  
		  #get a specific question
	def get(self,title_name):
		question=[question for question in questions if question["title"]==title_name]
		if len(question)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : question}),200)
		

	




