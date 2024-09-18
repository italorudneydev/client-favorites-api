from app.infrastructure.extensions import db

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    review_score = db.Column(db.Float, default=0, nullable=False)