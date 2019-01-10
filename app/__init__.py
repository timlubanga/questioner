from flask import Flask


def create_app():
   app = Flask(__name__)
   from api.v1 import version1 as v1 
   app.register_blueprint(v1)
   return app


