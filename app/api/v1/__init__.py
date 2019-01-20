from flask_restful import Api
from flask import Blueprint


from .meetup import Meetup
from .user import User
from .question import Question
from .get_all_meetups import Meetups
from .get_all_questions import Questions
from .get_all_users import Users
from .upvote import Upvotes
from .downvote import Downvotes
from .meetup_rsvp import RSVP

version1=Blueprint("api",__name__, url_prefix="/api/v1")
api=Api(version1)
api.add_resource(User,'/user')
api.add_resource(Meetup,'/meetup')
api.add_resource(Question,'/question')
api.add_resource(Meetups,'/meetups')
api.add_resource(Questions,'/questions')
api.add_resource(Users,'/users')
api.add_resource(Upvotes,'/question/upvote')
api.add_resource(Downvotes,'/question/downvote')
api.add_resource(RSVP,'/meetups/<topic_name>/rsvp')

