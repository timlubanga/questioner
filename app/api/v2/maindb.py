from dbconn import db_connection, destroy, execute_queries

def maindb(url):
	db_connection(url)
	destroy()
	execute_queries()

def test_main_db(url):
	db_connection(url)
	destroy()
	execute_queries()
	


