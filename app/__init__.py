from flask import Flask


def create_app():
   app = Flask(__name__)
   from .api.v2 import version2 as v2 
   app.register_blueprint(v2)
   return app


