import datetime as dt
from marshmallow import Schema,fields,post_load,ValidationError
from datetime import datetime
from pprint import pprint


class User:

    def __init__(self,*args,**kwargs):
        if 'name' in kwargs:
            self.first_name = kwargs['name'].split()[0]
            self.last_name = kwargs['name'].split()[1]
        else:
            self.first_name = kwargs['first_name']
            self.last_name = kwargs['last_name']
        self.email = kwargs.get('email')
        self.created_at = kwargs.get('created_at',datetime.now())

    def __repr__(self):
        return f"<User(name={self.first_name} {self.last_name} email={self.email})>"


class UserSchema(Schema):
    first_name = fields.String()
    last_name = fields.String()
    email = fields.Email()
    created_at = fields.DateTime()

    # In order to deserialize to an object, define a method of your Schema and decorate it
    # with post_load.  The method receives a dictionary of deserialized data.
    @post_load
    def make_user(self,data,**kwargs):
        if 'created_at' not in data.keys():
            data['created_at'] = datetime.now()
        return User(**data)


class BandMemberSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()


if __name__ == "__main__":

    # Serializing Python Objects
    user1 = User(name="Alan Rickman",email="alan.r@xyz.com")
    schema = UserSchema()
    result1 = schema.dump(user1)
    pprint(user1)
    pprint(result1)

    # Filter output fields
    email_schema = UserSchema(only=('last_name','email'))
    result1_1=email_schema.dump(user1)
    pprint(result1_1)

    # Deserializing objects("Loading")
    # reverse of dump method is load, validates and deserializes an input dict
    # to app level Data Structure. By default,it returns dictionary of field names
    # mapped to deserialized values
    user2_data = {
        'first_name':'John',
        'last_name':'Doe',
        'email':'john.d@abc.com',
        "created_at": "2014-08-11T05:26:03.869245"
    }
    user2 = schema.load(user2_data)
    print(user2)

    user3_data = {
        'first_name' : 'Alice',
        'last_name' : 'Newman'
    }

    user3 = schema.load(user3_data)
    print(user3)

    # Handling Collection of objects
    user4 = User(name="Mick Javier",email='mick.j@qrc.com')
    user5 = User(name="Chloe Morez",email="chloe.m@xzs.com")
    user6 = User(name="Linda Alvarez",email="linda.a@rte.com")
    users =[user4,user5,user6]
    res = schema.dump(users,many=True)
    pprint(res)

    # validation
    inv_user1 = {"name":"Linda Li","email":"werww"}
    try:
        schema.load(inv_user1)
    except ValidationError as e:
        print(e.messages)
        print(e.valid_data)

    band_members_data = [
    {'name':'Mick','email':'mick@stones.com'},
    {'name':'John','email':'Invalid'},
    {'email':'john@rock.com'},
    {'name':'kieth','email':'kieth@stones.com'}
    ]

    try:
        BandMemberSchema(many=True).load(band_members_data)
    except ValidationError as err:
        print(err.messages)

