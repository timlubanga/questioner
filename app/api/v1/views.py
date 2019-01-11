from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request

import datetime

app = Flask(__name__)
api = Api(app)



users=[]
class Users(Resource):
	def __init__(self):
	   self.id = len(users) + 1
	   #get a list of users

	   #create a new user
	def post(self,username):
		user=[user for user in users if user["username"]==username]
		if len(user)==0:
			new_user={"id":self.id,
		"firstname":request.json["firstname"],
		"lastname":request.json["lastname"],
		"othernames":request.json["othernames"],
		"email":request.json["email"],
		"phonenumber":request.json["phonenumber"],
		"username":request.json["username"],
		"registered":datetime.datetime.now(),
		"isAdmin":False,}
			users.append(new_user)
			return make_response(jsonify({
		   	"status" : 201,
		   	"data" : users}),201)
		else:
			return make_response(jsonify({"status":409,"error":"the record exists"}),409)
		#get one user
	def get(self,username):
		user=[user for user in users if user["username"]==username]
		if len(user)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "user does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : user}),200)
meetups=[]
class Meetups(Resource):
	def __init__(self):
	   self.id = len(users) + 1

	def post(self,topic_name):
		meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		if len(meetup)==0:
			new_meetup={
					"id":self.id,
					"CreatedOn":datetime.datetime.now(),
					"location":request.json["location"],
					"images":request.json["images"],
					"topic":request.json["topic"],
					"HappeningOn":request.json["HappeningOn"],
					"Tags":request.json["Tags"]
					}
			meetups.append(new_meetup)
			return make_response(jsonify({
		   	"status" : 201,
		   	"data" : meetups}),201)
		else:
			return make_response(jsonify({
		   	"status" : 409,
		   	"error" : "the record already exists"}),409)
		   	#get a specific meetup record
	def get(self,topic_name):
		meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		if len(meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : meetups}),200)

	def put(self,topic_name):
		new_meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		new_meetup[0]["HappeningOn"]=request.json["HappeningOn"]
		new_meetup[0]["Tags"]=request.json["Tags"]
		return make_response(jsonify({"status":202,"data":meetups}), 202)

	def delete(self, topic_name):
		meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		meetups.remove(meetup[0])
		return make_response(jsonify({"status":200,"data":meetups}), 200)  

questions=[]
class Questions(Resource):
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
					"title":request.json["title"],
					"body":request.json["body"],
					"votes":request.json["votes"]
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
	




