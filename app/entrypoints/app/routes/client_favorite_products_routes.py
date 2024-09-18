# from flask import Blueprint
# from app.entrypoints.app.controllers.client_favorite_products_controller import ClientFavoriteProductsController
#
#
# def create_client_favorite_products_bp(client_repository, product_repository):
#     controller = ClientFavoriteProductsController(client_repository, product_repository)
#     client_favorite_products_bp = Blueprint('client2', __name__, url_prefix='/client')
#
#     @client_favorite_products_bp.route('/favorites/add', methods=['POST'])
#     def add_favorite_product():
#         return controller.add_favorite_product()
#
#     return client_favorite_products_bp
