from flask import Flask,request
from flask_restful import Resource, reqparse,Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbdev:password@localhost:5432/portfolio'

api = Api(app)
db = SQLAlchemy(app)


class BankCustomer(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String,nullable=False)
    phone = db.Column(db.String,unique=True)


class BankAccount(db.Model):

    account_number = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String,nullable=False)
    account_balance = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer,db.ForeignKey(BankCustomer.id))
    user = db.relationship('BankCustomer',backref=db.backref('accounts',lazy=True))


user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument('name',required=True,type=str)
user_post_parser.add_argument('email',required=True,type=str)
user_post_parser.add_argument('phone',required=True,type=str)

user_patch_parser = reqparse.RequestParser()
user_patch_parser.add_argument('name',required=False,type=str)
user_patch_parser.add_argument('email',required=False,type=str)
user_patch_parser.add_argument('phone',required=False,type=str)

account_post_parser = reqparse.RequestParser()
account_post_parser.add_argument('account_name',type=str,required=True)
account_post_parser.add_argument('account_balance',type=int,required=False)
account_post_parser.add_argument('user_id',type=int,required=True)

account_patch_parser = reqparse.RequestParser()
account_patch_parser.add_argument('account_name',type=str,required=False)
account_patch_parser.add_argument('account_balance',type=int,required=False)


account_fields = {
    'account_number':fields.Integer,
    'account_name':fields.String,
    'account_balance':fields.Integer,
    'user_id':fields.Integer
}

account_without_user_fields = {
    'account_number':fields.Integer,
    'account_name':fields.String,
    'account_balance':fields.Integer
}

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'accounts': fields.Nested(account_without_user_fields)
}


class UserList(Resource):

    @marshal_with(user_fields)
    def get(self,id=None):
        if id is None:
            return BankCustomer.query.all()
        user = BankCustomer.query.filter_by(id=id).first()
        if not user:
            return {'message':'User not found'}, 404
        return user, 200


class AccountList(Resource):

    @marshal_with(account_fields)
    def get(self, id=None):
        if id is None:
            return BankAccount.query.all()
        account = BankAccount.query.filter_by(id=id).first()
        if not account:
            return {'message':'account not found'}, 404
        return account, 200


api.add_resource(UserList, '/users', '/users/<int:id>')
api.add_resource(AccountList, '/accounts', '/accounts/<int:id>')


@app.cli.command('reset_db')
def reset():
    db.drop_all()


@app.cli.command('bootstrap')
def initdb():
    db.drop_all()
    db.create_all()
    u1 = BankCustomer(name='Alice Stone',email='alice.st@outlook.com',phone='+1-232-098-083')
    u2 = BankCustomer(name='Bob Williams',email='bob.w@hotmail.com',phone='+1-112-098-083')
    u3 = BankCustomer(name='Roger Wilkinsons',email='roger.w@hotmail.com',phone='+1-232-112-083')

    a1 = BankAccount(account_name='12123AS',account_balance=340)
    a2 = BankAccount(account_name='12122AS',account_balance=700)
    a3 = BankAccount(account_name='00323BW',account_balance=500)
    a4 = BankAccount(account_name='01323RW')

    u1.accounts.append(a1)
    u1.accounts.append(a2)
    u2.accounts.append(a3)
    u3.accounts.append(a4)

    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.add(a4)

    db.session.commit()


#if __name__ == "__main__":
#    app.run()





