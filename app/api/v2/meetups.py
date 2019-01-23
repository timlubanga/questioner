
from .meetup import api,Meetup
from flask import jsonify, make_response, request
import psycopg2
import datetime
from psycopg2.extras import RealDictCursor

class Meetups(Meetup):
	def __init__(self):
			self.conn =  psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')
	
	#post a meetup to meetups

	def post(self):
		created_on=datetime.datetime.now(),
		location=request.json["location"],
		images=request.json["images"],
		topic=request.json["topic"],
		happeningOn=request.json["happeningOn"],
		tags=request.json["tags"],
		
		query = "SELECT * FROM meetups where topic = %s"
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		cur.execute(query, (topic, ))
		result = cur.fetchall()
		if result:
			return make_response(jsonify({"status":409,"error":"the record exists"}),409)
		
		new_meetup = "INSERT INTO meetups(created_on,location,images,topic,happeningOn,tags) VALUES(%s,%s,%s,%s,%s,%s)" 
		params = (created_on,location,images,topic,happeningOn,tags)
		cur.execute(new_meetup, params)

		self.conn.commit()
		cur.close()
		return {"message":"meetup successfully"}




	# retrieve all meetups from the database

	def get(self):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM meetups" 
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






