from gubr import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), index=True)
    first_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), index=True, unique=True)
    phone_number = db.Column(db.String(12), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.email}>'
