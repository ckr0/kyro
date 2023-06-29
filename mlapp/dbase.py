from . import db

class urldatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1500))
    category = db.Column(db.String(150))