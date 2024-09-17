from app.core.entities.client import Client
from app.core.repositories.client.client_repository_interface import ClientRepositoryInterface

class CreateClient:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, name: str, email: str):
        if self.client_repository.get_by_email(email):
            raise ValueError("Client with this email already exists")

        client = Client(name, email)
        self.client_repository.add(client)