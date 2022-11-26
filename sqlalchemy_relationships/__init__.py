from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbdev:xxxx@localhost:5432/portfolio'
db = SQLAlchemy(app)







