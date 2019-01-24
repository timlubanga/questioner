from marshmallow import Schema,fields, validate

not_blank = validate.Length(min=2, error='Field cannot be blank and should be atleast 2 characters')
class MeetupSchema(Schema):
	location=fields.String(required=True)
	images=fields.String(required=True,validate=not_blank)
	topic=fields.String(required=True,validate=not_blank)
	HappeningOn=fields.Date()
	Tags=fields.String(required=True, validate=not_blank)

class UserSchema(Schema):
	firstname=fields.String(required=True,validate=not_blank)
	lastname=fields.String(required=True,validate=not_blank)
	othernames=fields.String(required=True,validate=not_blank)
	email=fields.Email(required=True,validate=not_blank)
	phonenumber=fields.Integer(required=True)


class QuestionSchema(Schema):

	createdby=fields.Integer(required=True)
	meetup_id=fields.Integer()
	title=fields.String(required=True,validate=not_blank)
	body=fields.String(required=True,validate=not_blank)

class Meetup_rsvpSchema(Schema):
	user=fields.Integer()
	response=fields.String(required=True,validate=not_blank)

	


