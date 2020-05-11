import os
from sqla_wrapper import SQLAlchemy

db = SQLAlchemy(os.getenv("DATABASE_URL", "sqlite:///localhost.sqlite"))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    secret_number = db.Column(db.Integer, nullable=True)


class SecretNumberStore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookie_identifier = db.Column(db.String, unique=True, nullable=False)
    secret_number = db.Column(db.Integer, nullable=False)