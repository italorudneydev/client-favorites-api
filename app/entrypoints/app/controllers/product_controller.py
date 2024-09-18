from flask import request, jsonify
from app.core.use_cases.product.get_product_pagination import ListProductsPaginated
from app.core.use_cases.product.get_single_product import GetSingleProduct
from http import HTTPStatus

class ProductController:
    def __init__(self, repository):
        self.repository = repository

    def list_products_paginated(self):
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        use_case = ListProductsPaginated(self.repository)
        products_paginated = use_case.execute(page, per_page)

        return jsonify({
            "products": products_paginated["items"],
            "total": products_paginated["total"],
            "pages": products_paginated["pages"],
            "current_page": products_paginated["current_page"]
        }), HTTPStatus.OK

    def get_single_product(self, product_id):
        use_case = GetSingleProduct(self.repository)

        product = use_case.execute(product_id)

        if not product:
            return jsonify({"error": "Product not found"}), HTTPStatus.NOT_FOUND

        return jsonify(product), HTTPStatus.OK