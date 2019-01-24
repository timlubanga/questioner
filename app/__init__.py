from flask import Flask
from flask_jwt_extended import (create_access_token, JWTManager)


def create_app():
   app = Flask(__name__)
   app.config['JWT_SECRET_KEY'] = 'timothy'  
   jwt = JWTManager(app)
   
   from .api.v2 import version2 as v2 
   app.register_blueprint(v2)
   return app



