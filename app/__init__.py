from flask import Flask

from app import routes
from app.core import database, migrations, jwt


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    routes.init_app(app)

    return app
