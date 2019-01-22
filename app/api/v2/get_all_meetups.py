
from .meetup import api,Meetup
from flask import jsonify, make_response
import psycopg2

class Meetups(Meetup):
	def __init__(self):
			self.conn =  psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')
	# retrieve all meetups from the database
	def get(self):
		cur = self.conn.cursor()
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






