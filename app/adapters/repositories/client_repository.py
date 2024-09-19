from abc import ABC

from sqlalchemy.orm import Session
from app.core.entities.client import Client
from app.core.repositories.client_repository_interface import ClientRepositoryInterface


class ClientRepository(ClientRepositoryInterface, ABC):
    def __init__(self, session: Session):
        self.session = session

    def add(self, client: Client) -> None:
        self.session.add(client)
        self.session.commit()

    def get_by_email(self, email: str) -> Client | None:
        return self.session.query(Client).filter_by(email=email).first()

    def update(self, client: Client) -> None:
        existing_client = self.get_by_email(client.email)
        if existing_client:
            existing_client.name = client.name
            self.session.commit()

    def delete(self, email: str) -> None:
        client = self.get_by_email(email)
        if client:
            self.session.delete(client)
            self.session.commit()

    def save(self, client: Client) -> None:
        if client.id:
            self.update(client)
        else:
            self.add(client)