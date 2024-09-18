from abc import ABC, abstractmethod
from app.core.entities.product import Product


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Product | None:
        pass
