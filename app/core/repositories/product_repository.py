from abc import ABC

from sqlalchemy.orm import Session
from app.core.entities.product import Product
from app.core.repositories.product_repository_interface import ProductRepositoryInterface


class ProductRepository(ProductRepositoryInterface, ABC):
    def __init__(self, session: Session):
        self.session = session


    def get_by_id(self, id: int) -> Product | None:
        return self.session.query(Product).filter_by(id=id).first()


