
from .question import api
from flask import jsonify, make_response
from .utils.helper import Helpers
from flask_restful import Resource, Api
class Questions(Resource):

	def __init__(self):
		self.questions=Helpers()

	def get(self):
		result=self.questions.fetch_all_question_records()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" :  result}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "The question table is empty"}),200)



