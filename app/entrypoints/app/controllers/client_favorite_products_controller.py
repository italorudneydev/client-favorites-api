from flask import request, jsonify
from app.core.use_cases.client.add_favorite_product import AddFavoriteProduct
from http import HTTPStatus

class ClientFavoriteProductsController:
    def __init__(self, client_repository, product_repository):
        self.client_repository = client_repository
        self.product_repository = product_repository

    def add_favorite_product(self):
        data = request.json
        use_case = AddFavoriteProduct(self.client_repository, self.product_repository)
        try:
            use_case.execute(data.get('email'), data.get('product_id'))
            return jsonify({"message": "Product added to favorites successfully"}), HTTPStatus.OK
        except ValueError as e:
            return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST
