from flask import render_template
from gubr.forms import LoginForm
from gubr import app

from faker import Faker

fake = Faker()

@app.route('/')
@app.route('/home')
def home():
    user = {'username': fake.name()}
    bills = [
        {
            'bill': {'biller': fake.company()},
            'amount': 10
        },
        {
            'bill': {'biller': fake.company()},
            'amount': 20
        }
    ]
    return render_template('home.html', title='Home', user=user, bills=bills)


# login route - 
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)