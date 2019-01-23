from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
import datetime
from .utils.validator import UserSchema
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
api = Api(app)


class User(Resource):
	def __init__(self): 
	   self.validate=UserSchema()
	   self.conn = psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')
	   #get a list of users

	   #create a new user
	

		# GET a user with a spefic username
	def get(self,username):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query="SELECT * FROM users where username= %s".format("username")
		cur.execute(query,(username,))
		row=cur.fetchone()
		cur.close()
		if row:
			return make_response(jsonify({
		   	"status" : 200,

		   	"data" : row}),200)

		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "record not found"}),404)
	

