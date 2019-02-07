import psycopg2
from psycopg2.extras import RealDictCursor
from flask import request

class Helpers():
	def __init__(self):
		self.conn = psycopg2.connect(database = 'questioner', user = 'timo', password = 'smartjoker', host = 'localhost')
	
	def check_if_user_exists(self,username):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query="SELECT * FROM users where username= %s".format("username")
		cur.execute(query,(username,))
		result=cur.fetchone()
		return result
		cur.close()

	def check_if_user_exists_by_id(self,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query="SELECT * FROM users where username= %s".format("_id")
		cur.execute(query,(_id,))
		result=cur.fetchone()
		return result
		cur.close()

	def retriveve_all_users(self):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM users" 
		cur.execute(query)
		result = cur.fetchall()
		return result
		cur.close()

	def insert_new_user(self, params):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		new_user_query = "INSERT INTO users(firstname,lastname,othername,email,phone_number,username,registered,password,isadmin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
		params = (params['firstname'],params['lastname'],params['othername'],params['email'],params['phone_number'],params['username'],params['registered'],params['password'],params['isadmin'])
		cur.execute(new_user_query, params)

		self.conn.commit()
		cur.close()

	def check_if_ameetup_exist(self,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query="SELECT * FROM meetups where meetup_id=%s".format(_id)
		cur.execute(query,(_id,))
		row=cur.fetchone()
		return row
		cur.close()

	def insert_new_meetup(self,data,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		new_query="UPDATE meetups SET happeningon=%s,images=%s where meetup_id=%s".format(_id)
		cur.execute(new_query,(data['happeningon'], data['images'],_id),)
		self.conn.commit()
		cur.close()

	def delete_ameetup_record(self,_id):
		cur= self.conn.cursor(cursor_factory=RealDictCursor)
		new_query="DELETE from  meetups where meetup_id=%s".format(_id) 
		cur.execute(new_query,(_id))
		self.conn.commit()
		cur.close()

	def check_a_meetup_record_by_topic_name(self,topic):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM meetups where topic = %s"
		cur.execute(query, (topic, ))
		result = cur.fetchall()
		return result
		

	def post_ameetup_record(self,data):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)

		new_meetup = "INSERT INTO meetups(created_on,location,images,topic,happeningon,tags) VALUES(%s,%s,%s,%s,%s,%s)" 
		params = (data['created_on'],data['location'],data['images'],data['topic'],data['happeningon'],data['tags'])
		cur.execute(new_meetup, params)

		self.conn.commit()
		cur.close()

	def get_all_meetups(self):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM meetups" 
		cur.execute(query)
		result=cur.fetchall()
		return result


	def post_a_question(self,data):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		new_meetup = "INSERT INTO questions(createdon,createdby,meetup_id,title,body,upvotes,downvotes) VALUES(%s,%s,%s,%s,%s,%s,%s)" 
		params = (data['createdon'],data['createdby'],data['meetup_id'],data['title'],data['body'],data['upvotes'],data['downvotes'])
		cur.execute(new_meetup, params)
		
		self.conn.commit()
		cur.close()
	def check_if_a_question_exists(self,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM questions where id = %s".format(_id)
		cur.execute(query, (_id, ))
		result = cur.fetchall()
		return result
	def fetch_all_question_records(self):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		query = "SELECT * FROM questions" 
		cur.execute(query)
		result=cur.fetchall()
		return result
	
	def upvote_aquestion(self,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		new_query="UPDATE questions SET upvotes=upvotes+1 where id=%s".format(_id)
		cur.execute(new_query,(_id),)
		self.conn.commit()
		cur.close()

	def downvote_aquestion(self,_id):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)
		new_query="UPDATE questions SET downvotes=downvotes-1 where id=%s".format(_id)
		cur.execute(new_query,(_id),)
		self.conn.commit()
		cur.close()

	def post_rsvp(self,data):
		cur = self.conn.cursor(cursor_factory=RealDictCursor)

		new_meetup = "INSERT INTO rsvps(meetup_id,user_id,response) VALUES(%s,%s,%s)" 
		params = (data['meetup_id'],data['user_id'],data['response'])
		cur.execute(new_meetup,(params),)

		self.conn.commit()
		cur.close()






		

