from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.helper import check_if_a_question_exists
from flask_jwt_extended import jwt_required,get_jwt_identity



class Upvotes(Resource):

	@jwt_required
	def patch (self,_id):
		result=check_if_a_question_exists(_id)
		if result:
			self.question.upvote_aquestion(_id)

			return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "question upvoted successfully"}),200)
		else:
			return make_response(jsonify({
		   			"status" : 200,
		   			"message" : "The question does not exist"}),200)

	

		