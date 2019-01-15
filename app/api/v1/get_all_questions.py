
from .question import Question,api
from flask import jsonify, make_response
from .models import questions
class Questions(Question):
	def get(self):
		if len(questions)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"message" : "no record exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : questions}),200)



