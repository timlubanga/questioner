from marshmallow import Schema,fields, validate, ValidationError,validates, validates_schema

not_blank = validate.Length(min=2, error='Field cannot be blank and should be atleast 2 characters')
class MeetupSchema(Schema):
	location=fields.String(required=True,validate=not_blank)
	images=fields.String(required=True,validate=not_blank)
	topic=fields.String(required=True,validate=not_blank)
	Happeningon=fields.Date()
	tags=fields.String(required=True, validate=not_blank)

	@validates("location")
	def location_field(self, data):
		result=data.isalpha()
		if not result:
			raise ValidationError("the characters should be all alphabets only")
		res=data.isspace()
		if res:
			raise ValidationError("no whitespaces")

	@validates("topic")
	def topic_field(self, data):
		result=data.isalpha()
		res=data.isspace()
		if res:
			raise ValidationError("no whitespaces in this field")

		if not result:
			raise ValidationError("the characters should be all alphabets only")
		


class UserSchema(Schema):
	firstname=fields.String(required=True,validate=not_blank)
	lastname=fields.String(required=True,validate=not_blank)
	othername=fields.String(required=True,validate=not_blank)
	email=fields.Email(required=True,validate=not_blank)
	phone_number=fields.String(required=True)
	username=fields.String(required=True)

	@validates("firstname")
	def firstname_field(self, data):
		result=data.isalpha()
		if not result:
			raise ValidationError("the characters should be all alphabets only")
	
	@validates("lastname")
	def lastname_field(self, data):
		result=data.isalpha()
		if not result:
			raise ValidationError("the characters should be all alphabets only")

	@validates("othername")
	def othernames_field(self, data):
		result=data.isalpha()
		if not result:
			raise ValidationError("the characters should be digits only")


	@validates("phone_number")
	def username_field(self, data):
		result=data.isdigit()
		if not result:
			raise ValidationError("the characters should be digits only")

class QuestionSchema(Schema):

	createdby=fields.Integer(required=True)
	meetup_id=fields.Integer()
	title=fields.String(required=True,validate=not_blank)
	body=fields.String(required=True,validate=not_blank)

class Meetup_rsvpSchema(Schema):
	user_id=fields.Integer(required=True,)
	response=fields.String(required=True)

class Login(Schema):
	password=fields.String(required=True, validate=not_blank)
	username=fields.String(required=True, validate=not_blank)

	@validates("password")
	def input_fields(self, data):
		result=data.isspace()
		if result:
			raise ValidationError("no whitespaces")

	@validates("username")
	def username_field(self, data):
		result=data.isspace()
		if result:
			raise ValidationError("no whitespaces")
		

	






