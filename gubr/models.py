from datetime import datetime
from gubr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    phone_number = db.Column(db.String(12), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    deactivated_at = db.Column(db.DateTime, index=True)

    def __repr__(self):
        return f'<User {self.email}>'


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256), index=True)

    def __repr__(self):
        return f'<Service {self.name}>'


class User_Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))

    def __repr__(self):
        return f'<User Service [{self.user_id}][{self.service_id}]'
