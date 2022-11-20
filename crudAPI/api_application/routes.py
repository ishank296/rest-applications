from api_application import api,db
from flask_restful import Resource, reqparse
from .models import Todo
from .serializer import todo_serializer
from datetime import datetime

todo_parser = reqparse.RequestParser()
todo_parser.add_argument("name",type = str)
todo_parser.add_argument("description",type=str)
todo_parser.add_argument("completed",type=bool)
todo_parser.add_argument("created_at",type=lambda x: datetime.strptime(x,'%Y-%m-%d %H:%M:%S'))



class TodoList(Resource):

    def get(self):
        todos = Todo.query.all()
        todos_resp = todo_serializer(todos)
        return todos_resp

    def post(self):
        data = todo_parser.parse_args()
        new_obj = Todo(**data)
        db.session.add(new_obj)
        db.session.commit()
        data['created_at'] = str(data['created_at'])
        return data, 201


api.add_resource(TodoList,"/todos")