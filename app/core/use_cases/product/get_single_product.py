class GetSingleProduct:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, product_id: int):
        return self.product_repository.get_by_id_with_cache(product_id)