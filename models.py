from database import db

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    contactno = db.Column(db.BigInteger)