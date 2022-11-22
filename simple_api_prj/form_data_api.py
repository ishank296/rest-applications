from flask import Flask,request
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

book_details = dict()


class Book(Resource):

    def get(self,book_id):
        if book_id not in book_details:
            return {"message":f"Book with id {book_id} doesn't exists. Please check"}, 404
        return book_details[book_id]

    def post(self,book_id):
        if book_id in book_details:
            return {"message":f"Book with id {book_id} already registered"}
        book_info = {}
        for key in request.form:
            book_info[key] = request.form[key]
        book_details[book_id] = book_info
        return {"message": f"Book with id {book_id} added to list"}


api.add_resource(Book,'/books/<string:book_id>')


if __name__ == "__main__":
    app.run(debug=True)

