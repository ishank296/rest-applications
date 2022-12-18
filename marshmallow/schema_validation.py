from marshmallow import fields, Schema, validate, ValidationError, validates


class UserSchema(Schema):
    name = fields.String(required=True,validate=validate.Length(min=5))
    permission = fields.String(validate=validate.OneOf(['read','write','admin']))
    age = fields.Integer(validate=validate.Range(min=18,max=50))
    login_id = fields.String()

    @validates('login_id')
    def validate_login(self,value):
        if not (len(value) > 6 and value.isalnum()):
            raise ValidationError("login id must contains atleast one digit and one alphabet and "\
                                  "should be atleast seven digit")


if __name__ == "__main__":
    in_data = [
        {'name':'Joe','email':'joe@xyz.com','login_id':'joerog'},
        {'name':'Rick','age':56,'permission':'execute'}
    ]

    try:
        UserSchema(many=True).load(in_data)
    except ValidationError as err:
        print(err.messages)