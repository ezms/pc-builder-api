from os import getenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import models

db = SQLAlchemy()


def init_app(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.db = db

    models.get_models()