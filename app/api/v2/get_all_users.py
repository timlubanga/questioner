
from .user import User,api
from flask import jsonify, make_response, request
import psycopg2
import datetime
from psycopg2.extras import RealDictCursor
class Users(User):
	def __init__(self):
			self.conn =  psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')
	
	def post(self):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
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


	# retrieve all users from the database
	def get(self):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM users" 
		cur.execute(query)
		result = cur.fetchall()
		if result:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : result}),200)

		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "database is empty"}),200)






