from flask import Flask
from flask_cors import CORS

from app import routes
from app.core import database, email, jwt, migrations


def create_app():
    app = Flask(__name__)
    CORS(app)

    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    email.init_app(app)
    routes.init_app(app)

    return app
