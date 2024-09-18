from app.entrypoints.app.controllers.client_favorite_products_controller import ClientFavoriteProductsController

def register_client_favorite_products_routes(app, client_repository, product_repository):
    controller = ClientFavoriteProductsController(client_repository, product_repository)

    app.add_url_rule('/client/favorites/add', methods=['POST'], view_func=controller.add_favorite_product)