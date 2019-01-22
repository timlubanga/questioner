from flask_restful import Resource, Api
from flask import Flask, jsonify, make_response, request
from .models import meetups
from .utils.validator import MeetupSchema
import psycopg2

import datetime

app = Flask(__name__)
api = Api(app)


class Meetup(Resource):
	def __init__(self):
		self.validate=MeetupSchema()
		self.conn=psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')

	def post(self):
		created_on=datetime.datetime.now(),
		location=request.json["location"],
		images=request.json["images"],
		topic=request.json["topic"],
		happeningOn=request.json["happeningOn"],
		tags=request.json["tags"],
		_id=request.json["_id"]

					
		query = "SELECT * FROM meetups where id = %s"
		cur = self.conn.cursor()
		cur.execute(query, (request.json["_id"], ))
		result = cur.fetchall()
		if result:
			return make_response(jsonify({"status":409,"error":"the record exists"}),409)
		
		new_meetup = "INSERT INTO meetups(created_on,location,images,topic,happeningOn,tags,id) VALUES(%s,%s,%s,%s,%s,%s,%s)" 
		params = (created_on,location,images,topic,happeningOn,tags,_id)
		cur.execute(new_meetup, params)

		self.conn.commit()
		cur.close()
		return {"message":"meetup successfully"}
	def get(self):
		topic_name=request.json["topic"]
		meetup=[meetup for meetup in meetups if meetup["topic"]==topic_name]
		if len(meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		else:
			return make_response(jsonify({
		   	"status" : 200,
		   	"data" : meetup[0]}),200)

	def put(self):
		record_id=request.json["id"]
		new_meetup=[meetup for meetup in meetups if meetup["id"]==record_id]
		if len(new_meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		new_meetup[0]["HappeningOn"]=request.json["HappeningOn"]
		new_meetup[0]["Tags"]=request.json["Tags"]
		return make_response(jsonify({"status":202,"data":meetups}), 202)

	def delete(self):
		topic_id=request.json["id"]
		meetup=[meetup for meetup in meetups if meetup["id"]==topic_id]
		if len(meetup)==0:
			return make_response(jsonify({
		   	"status" : 200,
		   	"error" : "record does not exist"}),200)
		meetups.remove(meetup[0])
		return make_response(jsonify({"status":200,"data":meetups}), 200)  






