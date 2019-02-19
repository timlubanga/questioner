import psycopg2
from psycopg2.extras import RealDictCursor



def get_connection(url):

	global cur,connection
	conn=url
	connection=psycopg2.connect(conn)
	cur = connection.cursor(cursor_factory=RealDictCursor)
	
def check_if_user_exists(username):
	cur = connection.cursor(cursor_factory=RealDictCursor)
	query="SELECT * FROM users where username= %s".format("username")
	cur.execute(query,(username,))
	result=cur.fetchone()
	connection.commit()
	cur.close()
	return result
	

def check_if_user_exists_by_id(_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query="SELECT * FROM users where username= %s".format("_id")
	cur.execute(query,(_id,))
	result=cur.fetchone()
	connection.commit()
	cur.close()
	return result

def retriveve_all_users():
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query = "SELECT * FROM users" 
	cur.execute(query)
	result = cur.fetchall()
	connection.commit()
	cur.close()
	return result

def insert_new_user(params):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	new_user_query = "INSERT INTO users(firstname,lastname,othername,email,phone_number,username,registered,password,isadmin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
	params = (params['firstname'],params['lastname'],params['othername'],params['email'],params['phone_number'],params['username'],params['registered'],params['password'],params['isadmin'])
	cur.execute(new_user_query, params)
	connection.commit()
	cur.close()

def check_if_ameetup_exist(_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query="SELECT * FROM meetups where meetup_id=%s".format(_id)
	cur.execute(query,(_id,))
	row=cur.fetchone()
	connection.commit()
	cur.close()
	return row

def insert_new_meetup(data,_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	new_query="UPDATE meetups SET happeningon=%s,images=%s where meetup_id=%s".format(_id)
	cur.execute(new_query,(data['happeningon'], data['images'],_id),)
	connection.commit()
	cur.close()

def delete_ameetup_record(_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	new_query="DELETE from  meetups where meetup_id=%s".format(_id) 
	cur.execute(new_query,(_id))
	connection.commit()
	cur.close()

def check_a_meetup_record_by_topic_name(topic):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query = "SELECT * FROM meetups where topic = %s"
	cur.execute(query, (topic, ))
	result = cur.fetchall()
	connection.commit()
	cur.close()
	return result
		

def post_ameetup_record(data):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	new_meetup = "INSERT INTO meetups(created_on,location,images,topic,happeningon,tags) VALUES(%s,%s,%s,%s,%s,%s)" 
	params = (data['created_on'],data['location'],data['images'],data['topic'],data['happeningon'],data['tags'])
	cur.execute(new_meetup, params)

	connection.commit()
	cur.close()

def get_all_meetups():
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query = "SELECT * FROM meetups" 
	cur.execute(query)
	result=cur.fetchall()
	connection.commit()
	cur.close()
	return result


def post_a_question(data):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	new_meetup = "INSERT INTO questions(createdon,createdby,meetup_id,title,body,upvotes,downvotes) VALUES(%s,%s,%s,%s,%s,%s,%s)" 
	params = (data['createdon'],data['createdby'],data['meetup_id'],data['title'],data['body'],data['upvotes'],data['downvotes'])
	cur.execute(new_meetup, params)
		
	connection.commit()
	cur.close()
def check_if_a_question_exists(_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query = "SELECT * FROM questions where id = %s".format(_id)
	cur.execute(query, (_id, ))
	result = cur.fetchall()
	connection.commit()
	return result
def fetch_all_question_records():
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	query = "SELECT * FROM questions" 
	cur.execute(query)
	result=cur.fetchall()
	connection.commit()
	return result
	
def upvote_aquestion(_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)
	new_query="UPDATE questions SET upvotes=upvotes+1 where id=%s".format(_id)
	cur.execute(new_query,(_id),)
	connection.commit()
	cur.close()

def downvote_aquestion(_id):
	cur = connection.cursor(cursor_factory=RealDictCursor)	
	new_query="UPDATE questions SET downvotes=downvotes-1 where id=%s".format(_id)
	cur.execute(new_query,(_id),)
	connection.commit()
	cur.close()

def post_rsvp(data):
	cur = connection.cursor(cursor_factory=RealDictCursor)	

	new_meetup = "INSERT INTO rsvps(meetup_id,user_id,response) VALUES(%s,%s,%s)" 
	params = (data['meetup_id'],data['user_id'],data['response'])
	cur.execute(new_meetup,(params),)

	connection.commit()
	cur.close()






		

