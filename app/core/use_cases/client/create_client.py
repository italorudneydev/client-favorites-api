from app.core.entities.client import Client
from app.core.services.validation import validate_email, validate_required_fields
from app.core.repositories.client_repository_interface import ClientRepositoryInterface

class CreateClient:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, name: str, email: str):
        validate_required_fields(name, email)

        if not validate_email(email):
            raise ValueError("Invalid email format")

        if self.client_repository.get_by_email(email):
            raise ValueError("Client with this email already exists")

        client = Client(name, email)
        self.client_repository.add(client)