from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Fcuser(db.Model):
    __tablename__ = 'fcuser'
    userid = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(12))
