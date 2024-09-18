from abc import ABC
from app.core.entities.product import Product
from app.core.repositories.product_repository_interface import ProductRepositoryInterface
from app.core.interfaces.cache_interface import CacheInterface


class ProductRepository(ProductRepositoryInterface, ABC):
    def __init__(self, session, cache: CacheInterface):
        self.session = session
        self.cache = cache

    def get_by_id(self, id: int) -> Product | None:
        return self.session.query(Product).filter_by(id=id).first()

    def get_paginated_products(self, page: int, per_page: int):
        cache_key = f"products_page_{page}_per_page_{per_page}"

        cached_data = self.cache.get(cache_key)
        if cached_data:
            return cached_data

        paginated_result = self.session.query(Product).paginate(page=page, per_page=per_page, error_out=False)

        products_list = [{"id": p.id, "title": p.title, "price": p.price, "image": p.image, "brand": p.brand, "review_score": p.review_score} for p in paginated_result.items]

        result = {
            "items": products_list,
            "total": paginated_result.total,
            "pages": paginated_result.pages,
            "current_page": paginated_result.page,
            "per_page": paginated_result.per_page
        }

        self.cache.set(cache_key, result, timeout=300)

        return result

    def get_by_id_with_cache(self, product_id: int):
        cache_key = f"product_{product_id}"

        cached_product = self.cache.get(cache_key)
        if cached_product:
            return cached_product

        product = self.session.query(Product).filter_by(id=product_id).first()

        if not product:
            return None

        product_data = {
            "id": product.id,
            "title": product.title,
            "price": product.price,
            "image": product.image,
            "brand": product.brand,
            "review_score": product.review_score
        }

        self.cache.set(cache_key, product_data, timeout=300)

        return product_data


