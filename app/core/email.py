import os

from flask import Flask
from flask_mail import Mail


def init_app(app: Flask):

    mail_settings = {
        "MAIL_SERVER": os.getenv("MAIL_SERVER"),
        "MAIL_PORT": os.getenv("MAIL_PORT"),
        "MAIL_USERNAME": os.getenv("MAIL_USERNAME"),
        "MAIL_PASSWORD": os.getenv("MAIL_PASSWORD"),
        "MAIL_USE_TLS": True,
    }

    app.config.update(mail_settings)

    mail = Mail(app)
    mail.init_app(app)

    app.mail = mail
