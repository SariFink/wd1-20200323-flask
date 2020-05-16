import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    secret_number = db.Column(db.Integer, nullable=True)


class SecretNumberStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookie_identifier = db.Column(db.String, unique=True, nullable=False)
    secret_number = db.Column(db.Integer, nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, nullable=False)
    title = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=True)