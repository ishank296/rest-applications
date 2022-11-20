from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = '1275glhkikpl9087'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbdev:xxxx@localhost:5432/portfolio'

db = SQLAlchemy(app)

from api_application import routes

