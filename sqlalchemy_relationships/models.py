from sqlalchemy_relationships import db

# One To Many¶
# A one to many relationship places a foreign key on the child table referencing the parent.
# relationship() is then specified on the parent as referencing a collection of items
# represented by the child:

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


# Many to Many relationship
# Many to Many adds an association table between two classes.
# The association table is indicated by the relationship.secondary argument to relationship().

actors = db.Table(
    "actors",
     db.Column("actor_id",db.Integer,db.ForeignKey("actor.id")),
     db.Column("movie_id",db.Integer,db.ForeignKey("movie.id")),
)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime)
    actors = db.relationship("Actor",secondary=actors,backref="movies")


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)







