from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .utils.validator import MeetupSchema
import psycopg2
from psycopg2.extras import RealDictCursor



app = Flask(__name__)
api = Api(app)


class Meetup(Resource):
	def __init__(self):
		self.validate=MeetupSchema()
		self.conn=psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')


	def get(self,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query="SELECT * FROM meetups where meetup_id=%s".format(_id)
		cur.execute(query,(_id))
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

	def put(self,_id):
		happeningOn=request.json["happeningOn"]
		images=request.json["images"]
		cur = self.conn.cursor()
		query="SELECT * FROM meetups where meetup_id=%s".format(_id)
		cur.execute(query,(_id))
		row=cur.fetchone()
		if row:
			new_query="UPDATE meetups SET happeningOn=%s,images=%s where meetup_id=%s".format(_id)
			cur.execute(new_query,(happeningOn, images,_id))
			self.conn.commit()
			cur.close()
		
			return make_response(jsonify({
			"status":404,
			"message" : "record not found"}),404)
		
		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "record not found"}),404)


	
	def delete(self,_id):
		cur = self.conn.cursor()
		query="SELECT * FROM meetups where meetup_id=%s".format(_id)
		cur.execute(query,(_id))
		row=cur.fetchone()
		if row:
			new_query="DELETE from  meetups where meetup_id=%s".format(_id) 
			cur.execute(new_query,(_id))
			self.conn.commit()
			cur.close()
			return make_response(jsonify({
		   	"status":200,
		   	"message" : "record deleted successfully"}),200)
		else:
			return make_response(jsonify({
		   	"status":404,
		   	"message" : "record not found"}),404)

	



