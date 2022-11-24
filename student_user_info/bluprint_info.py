from flask import Blueprint
from flask_restful import Resource,Api

info = Blueprint('info',__name__,url_prefix='/info')
api = Api(info)


class StudentInfo(Resource):

    def get(self):
        return {'message':'Get Request for Student Info'}

    def post(self):
        return {'message':'Post Request for Student Info'}


api.add_resource(StudentInfo,'/student')