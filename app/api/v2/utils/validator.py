from marshmallow import Schema,fields, validate

not_blank = validate.Length(min=2, error='Field cannot be blank and should be atleast 2 characters')
class MeetupSchema(Schema):
	location=fields.String(required=True,validate=not_blank)
	images=fields.String(required=True,validate=not_blank)
	topic=fields.String(required=True,validate=not_blank)
	Happeningon=fields.Date()
	tags=fields.String(required=True, validate=not_blank)

class UserSchema(Schema):
	firstname=fields.String(required=True,validate=not_blank)
	lastname=fields.String(required=True,validate=not_blank)
	othername=fields.String(required=True,validate=not_blank)
	email=fields.Email(required=True,validate=not_blank)
	phone_number=fields.Integer(required=True)


class QuestionSchema(Schema):

	createdby=fields.Integer(required=True)
	meetup_id=fields.Integer()
	title=fields.String(required=True,validate=not_blank)
	body=fields.String(required=True,validate=not_blank)

class Meetup_rsvpSchema(Schema):
	user_id=fields.Integer(required=True)
	response=fields.String(required=True,validate=not_blank)




