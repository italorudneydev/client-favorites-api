from app.core.repositories.client.client_repository_interface import ClientRepositoryInterface

class GetClient:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, email: str):
        client = self.client_repository.get_by_email(email)
        if not client:
            raise ValueError("Client not found")
        return client