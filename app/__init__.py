from flask import Flask
from flask_jwt_extended import JWTManager
import os
import sys
topdir = os.path.join(os.path.dirname(__file__),"../" )
sys.path.append(topdir)
from instance.config import app_config
from .api.v2.maindb import maindb, test_main_db
from .api.v2.utils.helper import get_connection


def create_app(name_conf):
	app = Flask(__name__,instance_relative_config=True)
	app.config.from_object(app_config[name_conf])
	app.config['JWT_SECRET_KEY'] = 'timothy'  
	jwt = JWTManager(app)
	app.config.from_pyfile('config.py')
	db_url = app_config[name_conf].DATABASE_URL
	from .api.v2 import version2 as v2
	app.register_blueprint(v2)
	if db_url=="questioner_db":
		maindb(db_url)
	else:
		test_main_db(db_url)

	get_connection(db_url)
	return app

