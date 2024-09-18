class ListProductsPaginated:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, page=1, per_page=10):
        return self.product_repository.get_paginated_products(page, per_page)