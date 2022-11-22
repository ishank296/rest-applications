from flask import Flask
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    def get(self):
        return {'message': 'Hello World from Get Request'}

    def post(self):
        return {'message': 'This is response for POST request'}

    def put(self):
        return {'message': 'This is response for PUT request'}

    def delete(self):
        return {'message': 'This is response for DELETE request'}

api.add_resource(HelloWorld,'/greetings')

if __name__ == "__main__":
    app.run()
