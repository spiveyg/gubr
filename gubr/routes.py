from flask import render_template
from faker import Faker
from gubr import app

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