from sqlalchemy_relationships import db

# One To Many¶
# A one to many relationship places a foreign key on the child table referencing the parent.
# relationship() is then specified on the parent
#

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String,nullable=False)
    user_email = db.Column(db.String,nullable=False)
    accounts = db.relationship('Account')


class Account(db.Model):
    account_id = db.Column(db.Integer,primary_key=True)
    account_name = db.Column(db.String,nullable=False)
    account_balance = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer,db.ForeignKey(User.user_id))






