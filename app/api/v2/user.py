from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
import datetime
from .utils.validator import UserSchema
import psycopg2

app = Flask(__name__)
api = Api(app)


class User(Resource):
	def __init__(self): 
	   self.id = len(users) + 1
	   self.validate=UserSchema()
	   self.conn = psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')
	   #get a list of users

	   #create a new user
	def post(self):
		cur = self.conn.cursor()
		firstname=request.json["firstname"]
		lastname=request.json["lastname"]
		othername=request.json["othername"]
		email=request.json["email"]
		phone_number=request.json["phone_number"]
		username=request.json["username"]
		registered=datetime.datetime.now()
		password=request.json["password"]
		isadmin=False
		query = "SELECT * FROM users where username = %s"
		cur.execute(query, (username, ))
		result = cur.fetchall()
		if result:
			return make_response(jsonify({"status":409,"error":"the record exists"}),409)
		
		new_user_query = "INSERT INTO users(firstname,lastname,othername,email,phone_number,username,registered,password,isadmin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
		params = (firstname,lastname,othername,email,phone_number,username,registered,password,isadmin)
		cur.execute(new_user_query, params)

		self.conn.commit()
		cur.close()
		return "user created successfully"

		# GET a user with a spefic username
	def get(self):
		username=request.json["username"]
		cur = self.conn.cursor()
		query="SELECT * FROM users where username=%s"
		cur.execute(query,(username,))
		row=cur.fetchall()
		cur.close()
		if row:
			return make_response(jsonify({
		   	"status" : 200,

		   	"data" : row}),200)

		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "record not found"}),404)
	

