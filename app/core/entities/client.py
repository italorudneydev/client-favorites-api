from app.infrastructure.extensions import db
from app.core.validators.email_validator import EmailValidator

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, index=True, unique=True)

    def __init__(self, name: str, email: str):
        self.name = name
        if not EmailValidator.is_valid(email):
            raise ValueError("Invalid email format")
        self.email = email