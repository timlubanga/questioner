from flask_restful import Api
from flask import Blueprint


from .meetup import Meetup
from .user import User
from .question import Question
from .meetups import Meetups
from .get_all_questions import Questions
from .get_all_users import Users
from .upvote import Upvotes
from .downvote import Downvotes
from .meetup_rsvp import RSVP

version2=Blueprint("api",__name__, url_prefix="/api/v2")
api=Api(version2)
api.add_resource(User,'/user/<username>')
api.add_resource(Meetup,'/meetup/<_id>')
api.add_resource(Question,'/question')
api.add_resource(Meetups,'/meetups')
api.add_resource(Questions,'/questions')
api.add_resource(Users,'/users')
api.add_resource(Upvotes,'/question/upvote')
api.add_resource(Downvotes,'/question/downvote')
api.add_resource(RSVP,'/meetups/<topic_name>/rsvp')
