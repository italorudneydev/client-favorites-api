from flask import request, jsonify
from app.core.use_cases.client.create_client import CreateClient
from app.core.use_cases.client.get_client import GetClient
from app.core.use_cases.client.update_client import UpdateClient
from app.core.use_cases.client.delete_client import DeleteClient
from http import HTTPStatus

class ClientController:
    def __init__(self, repository):
        self.repository = repository

    def create_client(self):
        data = request.json
        use_case = CreateClient(self.repository)
        try:
            use_case.execute(data['name'], data['email'])
            return jsonify({"message": "Client created successfully"}), HTTPStatus.CREATED
        except ValueError as e:
            return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

    def get_client(self, email):
        use_case = GetClient(self.repository)
        try:
            client = use_case.execute(email)
            return jsonify({"name": client.name, "email": client.email}), HTTPStatus.OK
        except ValueError as e:
            return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND

    def update_client(self, email):
        data = request.json
        use_case = UpdateClient(self.repository)
        try:
            use_case.execute(data['name'], email)
            return jsonify({"message": "Client updated successfully"}), HTTPStatus.OK
        except ValueError as e:
            return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND

    def delete_client(self, email):
        use_case = DeleteClient(self.repository)
        try:
            use_case.execute(email)
            return jsonify({"message": "Client deleted successfully"}), HTTPStatus.OK
        except ValueError as e:
            return jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND
