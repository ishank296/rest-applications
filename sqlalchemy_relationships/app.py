from sqlalchemy_relationships import app,db
from .models import Account, User

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






