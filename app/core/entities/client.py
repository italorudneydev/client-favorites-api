from app.infrastructure.extensions import db
from app.core.entities.client_favorite_products import client_favorite_products


class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    favorite_products = db.relationship('Product', secondary=client_favorite_products,
                                        backref=db.backref('favored_by', lazy='dynamic'))

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email