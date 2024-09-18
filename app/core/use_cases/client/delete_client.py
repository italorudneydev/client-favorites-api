from app.core.repositories.client_repository_interface import ClientRepositoryInterface

class DeleteClient:
    def __init__(self, client_repository: ClientRepositoryInterface):
        self.client_repository = client_repository

    def execute(self, email: str):
        client = self.client_repository.get_by_email(email)
        if not client:
            raise ValueError("Client not found")

        self.client_repository.delete(email)