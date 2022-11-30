import argparse

from flask_authentication import db,app,api
from flask_restful import Resource, marshal_with, fields, reqparse
import uuid

todo_fields_without_user = {
    'id': fields.Integer,
    'text': fields.String,
    'complete': fields.Boolean
}

user_fields = {
    'public_id': fields.String,
    'name': fields.String,
    'admin': fields.Boolean,
    'todo_list': fields.Nested(todo_fields_without_user)
}


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    public_id = db.Column(db.String(50),nullable=False,unique=True)
    name = db.Column(db.String,nullable=False)
    password = db.Column(db.String)
    admin = db.Column(db.Boolean)
    todo_list = db.relationship("Todo")


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    complete = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))


user_parser = reqparse.RequestParser()
user_parser.add_argument('name',required=True,type=str)
user_parser.add_argument('password',required=True,type=str)


class Users(Resource):

    @marshal_with(user_fields)
    def get(self, id):
        if id is None:
            return User.query.all()
        user = User.query.get(id)
        if user:
            return user
        return {'message':f'User with id: {id} not found'}, 404


class Todolist(Resource):

    @marshal_with(todo_fields_without_user)
    def get(self, id):
        if id is None:
            return Todo.query.all()
        todo_item = Todo.query.get(id)
        if todo_item:
            return todo_item
        return {'message':'Resource not found'}, 404


api.add_resource(Users,'/users','/users/<int:id>')
api.add_resource(Todolist,'/todo','/todo/<int:id>')


@app.cli.command("init_db")
def init():
    db.create_all()


@app.cli.command("delete_db")
def init():
    db.drop_all()



