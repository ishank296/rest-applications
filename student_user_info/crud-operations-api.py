from flask_restful import Resource,Api
from flask_restful import reqparse,marshal_with, fields
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbdev:xxx@localhost:5432/portfolio'
db = SQLAlchemy(app)
api = Api(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    phone = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    course = db.Column(db.String(100))


db.create_all()

student_info_reqparser = reqparse.RequestParser()
student_info_reqparser.add_argument('name',type=str,required=True,help='Student name is required')
student_info_reqparser.add_argument('phone',type=str,required=True,help='Student phone is required')
student_info_reqparser.add_argument('course',type=str,help='Course ID in which student enrolled')
student_info_reqparser.add_argument('email',type=str,required=True)

student_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'phone': fields.String,
    'course': fields.String
}


class StudentList(Resource):

    @marshal_with(student_fields)
    def get(self,id = None):
        status = 500
        if id is not None:
            student = Student.query.filter_by(id=id).first()
            if student:
                status = 200
            else:
                status = 404
            return student, status
        else:
            return Student.query.all(), 200

    def post(self):
        args = student_info_reqparser.parse_args()
        student = Student(name=args['name'],
                          email=args['email'],
                          phone=args['phone'],
                          course=args['course'])
        db.session.add(student)
        db.session.commit()
        return {'message':'student created successfully'}


api.add_resource(StudentList,'/students','/students/<int:id>')


if __name__ == "__main__":
    app.run(debug=True)





