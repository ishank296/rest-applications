from sqlalchemy_relationships import app,db
from .models import Account, User, Actor, Movie
from datetime import datetime

@app.cli.command('initdb')
def reset_db():
    db.drop_all()
    db.create_all()


@app.cli.command('bootstrap')
def init_db():
    db.drop_all()
    db.create_all()
    u1 = User(user_name='Alice', user_email='alice@xxxm.com')
    u2 = User(user_name='Rob', user_email='robwe@xxxl.com')
    u3 = User(user_name='John', user_email='joxxn@xxxm.com')

    a1 = Account(account_name='ABED123',account_balance=100)
    a2 = Account(account_name='QEVE095', account_balance=0)
    a3 = Account(account_name='BSRH098', account_balance=340)
    a4 = Account(account_name='PLNH786', account_balance=220)

    m1 = Movie(title="Evil Dead", release_date=datetime.strptime("Oct 15 1981", "%b %d %Y"))
    m2 = Movie(title="Darkman", release_date=datetime.strptime("Aug 24 1990", "%b %d %Y"))
    m3 = Movie(title="The Quick and the Dead",
               release_date=datetime.strptime("Feb 10 1995", "%b %d %Y"))
    m4 = Movie(title="The Gift", release_date=datetime.strptime("Jan 19 2001", "%b %d %Y"))
    m5 = Movie(title="Army of Darkness",release_date=datetime.strptime("Feb 19 1993", "%b %d %Y") )

    bruce = Actor(name="Bruce Campbell")
    ellen = Actor(name="Ellen Sandweiss")
    hal = Actor(name="Hal Delrich")
    keeanu = Actor(name="Keeanu Reeves")
    betsy = Actor(name="Betsy Baker")
    liam = Actor(name="Liam Neeson")
    cate = Actor(name="Cate Blanchett")
    sharon = Actor(name="Sharon Stone")

    db.session.add(m1)
    db.session.add(m2)
    db.session.add(m3)
    db.session.add(m4)
    db.session.add(m5)

    db.session.add(bruce)
    db.session.add(sharon)
    db.session.add(cate)
    db.session.add(keeanu)
    db.session.add(liam)
    db.session.add(betsy)
    db.session.add(hal)
    db.session.add(ellen)

    m1.actors.extend((bruce,ellen,betsy))
    m2.actors.extend((bruce,liam))
    m3.actors.extend((bruce,sharon))
    m4.actors.extend((bruce,cate,keeanu))
    m5.actors.append(bruce)

    db.session.commit()




    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)

    db.session.add(a1)
    db.session.add(a2)
    db.session.add(a3)
    db.session.add(a4)

    u1.accounts.append(a1)
    u2.accounts.append(a2)
    u3.accounts.append(a3)
    u3.accounts.append(a4)
    db.session.commit()




@app.cli.command('check_data')
def print_data():
    users = User.query.all()
    user_list = list()
    for user in users:
        user_obj = dict()
        user_obj['user_id'] = user.user_id
        user_obj['user_name'] = user.user_name
        user_obj['email'] = user.user_email
        user_obj['accounts'] = [account.account_name for account in user.accounts]
        user_list.append(user_obj)
    for user in user_list:
       print(user)






