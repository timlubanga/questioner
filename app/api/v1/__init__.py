from flask_restful import Api
from flask import Blueprint


from views import Users,Meetups,Questions
version1=Blueprint("api",__name__, url_prefix="/api/v1")
api=Api(version1)
api.add_resource(Users,'/<username>')
api.add_resource(Meetups,'/meetup/<topic_name>')
api.add_resource(Questions,'/question/<title_name>')

