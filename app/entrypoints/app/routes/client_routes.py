from app.entrypoints.app.controllers.client_controller import ClientController

def register_client_routes(app, client_repository):
    client_controller = ClientController(client_repository)

    app.add_url_rule('/clients', methods=['POST'], view_func=client_controller.create_client)
    app.add_url_rule('/clients/<email>', methods=['GET'], view_func=client_controller.get_client)
    app.add_url_rule('/clients/<email>', methods=['PUT'], view_func=client_controller.update_client)
    app.add_url_rule('/clients/<email>', methods=['DELETE'], view_func=client_controller.delete_client)