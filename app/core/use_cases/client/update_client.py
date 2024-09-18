from app.core.repositories.client_repository_interface import ClientRepositoryInterface

class UpdateClient:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, name: str, email: str):
        client = self.client_repository.get_by_email(email)
        if not client:
            raise ValueError("Client not found")

        existing_client = self.client_repository.get_by_email(email)
        if existing_client and existing_client != client:
            raise ValueError("Another client with this email already exists")

        client.name = name
        client.email = email
        self.client_repository.update(client)