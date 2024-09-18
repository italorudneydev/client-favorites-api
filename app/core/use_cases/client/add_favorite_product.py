from app.core.repositories.client_repository_interface import ClientRepositoryInterface
from app.core.repositories.product_repository_interface import ProductRepositoryInterface

class AddFavoriteProduct:
    def __init__(self, client_repository: ClientRepositoryInterface, product_repository: ProductRepositoryInterface):
        self.client_repository = client_repository
        self.product_repository = product_repository

    def execute(self, email: str, product_id: int):
        client = self.client_repository.get_by_email(email)
        product = self.product_repository.get_by_id(product_id)
        if not client:
            raise ValueError("client does not exist")
        if not product:
            raise ValueError("Product does not exist")
        if product in client.favorite_products:
            raise ValueError("Product is already in the favorite list")
        client.favorite_products.append(product)
        self.client_repository.save(client)
