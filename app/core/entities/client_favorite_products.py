from app.infrastructure.extensions import db

client_favorite_products = db.Table('client_favorite_products',
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)