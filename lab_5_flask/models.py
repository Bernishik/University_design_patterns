from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Post(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(20))
    lastname = db.Column(db.String(20), nullable=False)
    age = db.Column(db.INTEGER, nullable=False)
    comment = db.Column(db.String(20), nullable=False)
