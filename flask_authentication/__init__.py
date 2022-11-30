from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['secret_key'] = "a4f4a831bcf34ba7a2be7fca8b6caa39"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbdev:xxxxx@localhost:5432/portfolio'
api = Api(app)
db = SQLAlchemy(app)

