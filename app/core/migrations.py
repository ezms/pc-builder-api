from flask_migrate import Migrate
from flask import Flask


def init_app(app: Flask):
    Migrate(app=app, db=app.db, compare_type=True)
