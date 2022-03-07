import locale
import os
from datetime import datetime

from flask import current_app, render_template
from flask_jwt_extended import get_jwt_identity
from flask_mail import Mail, Message

from app.core.database import db
from app.models.order_model import OrdersModel
from app.models.order_product_model import OrdersProductsModel
from app.models.product_model import ProductModel

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


def send_email_to_client(address, order_id, date):

    mail: Mail = current_app.mail

    user = get_jwt_identity()

    products = (
        db.session.query(ProductModel.model, ProductModel.price)
        .select_from(ProductModel)
        .join(OrdersProductsModel)
        .join(OrdersModel)
        .filter(OrdersProductsModel.order_id == order_id)
    )

    column_names = [column["name"] for column in products.column_descriptions]

    products = [dict(zip(column_names, prod)) for prod in products.all()]

    total = sum([prod["price"] for prod in products])

    # alterar o padrão de exibição dos valores dos produtos, para o tipo moeda R$
    products = [
        {
            key: locale.currency(val) if key == "price" else val
            for key, val in prod.items()
        }
        for prod in products
    ]

    address = {
        "CEP": address.zip_code,
        "Número": address.number,
        "Logradouro": address.public_place,
        "Cidade": address.city,
        "Estado": address.state,
    }

    msg = Message(
        subject="Resumo de Pedido - PC Builder",
        sender=os.getenv("MAIL_USERNAME"),
        recipients=[user["email"]],
        html=render_template(
            "order.html",
            products=products,
            total=locale.currency(total),
            username=user["name"],
            date=datetime.strftime(date, "%d/%m/%Y às %H:%M:%S"),
            address=address,
        ),
    )

    mail.send(msg)
