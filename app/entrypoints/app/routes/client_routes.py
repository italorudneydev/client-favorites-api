from flask import Blueprint
from app.entrypoints.app.controllers.client_controller import ClientController

def create_client_bp(client_repository):
    client_controller = ClientController(client_repository)
    client_bp = Blueprint('client', __name__)

    @client_bp.route('', methods=['POST'])
    def create_client():
        return client_controller.create_client()

    @client_bp.route('/<email>', methods=['GET'])
    def get_client(email):
        return client_controller.get_client(email)

    @client_bp.route('/<email>', methods=['PUT'])
    def update_client(email):
        return client_controller.update_client(email)

    @client_bp.route('/<email>', methods=['DELETE'])
    def delete_client(email):
        return client_controller.delete_client(email)

    return client_bp
