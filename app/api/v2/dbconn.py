import os
import psycopg2

class DbConnection:

    def db_connection(self):
        """ initilizes a connection with the database """
        self.conn = psycopg2.connect(database = 'questioner_db', user = 'postgres',password="password", host = 'localhost')
        return self.conn

    def get_connection(self):
        """ Returns a database connection """
        return self.conn

    def db_destroy(self):
        """ Deletes all records from the Database """
        DROP_DATABASE = """
                DROP SCHEMA public CASCADE;
                CREATE SCHEMA public;
                GRANT USAGE ON SCHEMA public TO postgres;
        """
        return DROP_DATABASE

    def create_database_tables(self):
        """ Create all database tables """

        TABLE_USERS = """ 
                             CREATE TABLE IF NOT EXISTS users (
                                Id serial PRIMARY KEY NOT NULL,
                                firstname VARCHAR (40) NOT NULL, 
                                lastname VARCHAR (40) NOT NULL, 
                                othername VARCHAR (40),
                                email VARCHAR (40) UNIQUE NOT NULL, 
                                phone_number VARCHAR (40),
                                username VARCHAR (40) UNIQUE NOT NULL,
                                registered TIMESTAMP NOT NULL DEFAULT current_timestamp, 
                                password VARCHAR (256) NOT NULL,
                                IsAdmin VARCHAR (20) DEFAULT false
        );"""

        TABLE_MEETUPS = """ 
                            CREATE TABLE IF NOT EXISTS meetups (
                                meetup_id serial PRIMARY KEY NOT NULL,
                                topic VARCHAR (90) NOT NULL,
                                happeningOn TIMESTAMP NOT NULL,
                                location VARCHAR (90) NOT NULL,
                                created_on TIMESTAMP NOT NULL DEFAULT current_timestamp,
                                images VARCHAR (200) NULL,
                                tags VARCHAR(200) NULL
        );"""

        TABLE_QUESTIONS = """ 
                        CREATE TABLE IF NOT EXISTS questions (
                            Id serial PRIMARY KEY NOT NULL,
                            meetup_id INTEGER  NOT NULL, 
                            createdby INTEGER NOT NULL, 
                            createdon TIMESTAMP NOT NULL DEFAULT current_timestamp,
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

    def execute_queries(self):
        curs = self.get_connection().cursor()
        #curs.execute(self.db_clean())
        for query in self.create_database_tables():
            curs.execute(query)
            self.get_connection().commit()

        

    def commit_changes(self):
        """ Commits changes to database """    
        self.get_connection().commit()

    def setUpTestDb(self):
        """ Sets up a test database """
        self.execute_queries()
        self.db_clean()


db = DbConnection()
db.db_connection()
db.execute_queries()
db.commit_changes()
