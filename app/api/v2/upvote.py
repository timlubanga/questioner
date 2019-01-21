from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import questions



class Upvotes(Resource):

	def patch (self):
		question_id=request.json["id"]
		question=[question for question in questions if question["id"]==question_id]
		if len(question)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		else:
			question[0]["upvotes"] = question[0]["upvotes"]+1
			return make_response(jsonify({
		   			"status" : 200,
		   			"data" : question}),200)

		return make_response(jsonify({
		   		"status" : 404,
		   		"error" : "the database is empty"}),404)

		