
import psycopg2

def db_connection(url):

    global cur,connection
    connection=psycopg2.connect(url)
    cur = connection.cursor()

def db_destroy():
    DROP_DATABASE = """
                DROP SCHEMA public CASCADE;
                CREATE SCHEMA public;
                GRANT USAGE ON SCHEMA public TO postgres;
        """
    return DROP_DATABASE

def create_database_tables():

    TABLE_USERS = """ 
                        CREATE TABLE IF NOT EXISTS users (
                                Id serial PRIMARY KEY NOT NULL,
                                firstname VARCHAR (40) NOT NULL, 
                                lastname VARCHAR (40) NOT NULL, 
                                othername VARCHAR (40),
                                email VARCHAR (40) UNIQUE NOT NULL, 
                                phone_number VARCHAR (40),
                                username VARCHAR (40) UNIQUE NOT NULL,
                                registered TIMESTAMP NOT NULL, 
                                password VARCHAR (256) NOT NULL,
                                IsAdmin VARCHAR (20)
        );"""

    TABLE_MEETUPS = """ 
                        CREATE TABLE IF NOT EXISTS meetups (
                                meetup_id serial PRIMARY KEY NOT NULL,
                                topic VARCHAR (90) NOT NULL,
                                happeningOn TIMESTAMP NOT NULL,
                                location VARCHAR (90) NOT NULL,
                                created_on TIMESTAMP NOT NULL,
                                images VARCHAR (200) NULL,
                                tags VARCHAR(200) NULL
        );"""

    TABLE_QUESTIONS = """ 
                    CREATE TABLE IF NOT EXISTS questions (
                            Id serial PRIMARY KEY NOT NULL,
                            meetup_id INTEGER  NOT NULL, 
                            createdby INTEGER NOT NULL, 
                            createdon TIMESTAMP NOT NULL,
                            title VARCHAR (150) NOT NULL,
                            body VARCHAR (1000) NOT NULL, 
                            upvotes INTEGER DEFAULT 0,  
                            downvotes INTEGER DEFAULT 0 
                                       
        );"""
    TABLE_RSVPS = """ 
                    CREATE TABLE IF NOT EXISTS rsvps (
                            Id serial PRIMARY KEY NOT NULL,
                            meetup_id INTEGER NOT NULL, 
                            user_id INTEGER NOT NULL, 
                            response VARCHAR (200)
        );"""

    ADMIN_USER = """
                        INSERT INTO users(firstname,lastname,
                                          othername,email,phone_number,
                                          username,registered,password,isadmin) VALUES(
                            'Super Admin',
                            'timothy',
                            'lubanga',
                            'timlubanga@gmail.com',
                            '0714568338',
                            'timo',
                            current_timestamp,
                            'tim@lubanga',
                            true
                        )
        """

    return [TABLE_USERS,TABLE_MEETUPS,TABLE_QUESTIONS,TABLE_RSVPS,ADMIN_USER]

def execute_queries():
    cur = connection.cursor()
        #curs.execute(self.db_clean())
    for query in create_database_tables():
            cur.execute(query)
            connection.commit() 

def drop_table_queries():
    drop_queries = [
        "DROP TABLE IF EXISTS users CASCADE",
        "DROP TABLE IF EXISTS meetups CASCADE",
        "DROP TABLE IF EXISTS questions CASCADE",
        "DROP TABLE IF EXISTS rsvps CASCADE",
        "DROP TABLE IF EXISTS comments CASCADE",
        "DROP TABLE IF EXISTS votes CASCADE"
        ]
    return drop_queries

def destroy():
    cur = connection.cursor()
    queries = drop_table_queries()
    for query in queries:
        cur.execute(query)
    connection.commit()

    



