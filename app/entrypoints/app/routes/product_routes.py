from flask import Blueprint
from app.entrypoints.app.controllers.product_controller import ProductController

def create_product_bp(repository):
    controller = ProductController(repository)
    product_bp = Blueprint('product', __name__)

    @product_bp.route('/product/', methods=['GET'])
    def get_products_paginate():
        return controller.list_products_paginated()

    @product_bp.route('/product/<int:product_id>/', methods=['GET'])
    def get_single_product(product_id):
        return controller.get_single_product(product_id)

    return product_bp
