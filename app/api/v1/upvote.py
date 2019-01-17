from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import questions



class Upvotes(Resource):

	def patch (self,title_name):
		for question in questions:
			if question["title"] == title_name:
				question["upvotes"] = question["upvotes"]+1
				return make_response(jsonify({
		   			"status" : 200,
		   			"data" : question}),200)

			return make_response(jsonify({
		   	"status" : 404,
		   	"error" : "question does not exist"}),404)
		return make_response(jsonify({
		   		"status" : 404,
		   		"error" : "the database is empty"}),404)

		