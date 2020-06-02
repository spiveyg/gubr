from flask import (render_template, flash, redirect,)
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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f'Login requested for user {form.username.data}, \
            remember_me={form.remember_me.data}')
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)