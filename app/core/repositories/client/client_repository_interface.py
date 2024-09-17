from abc import ABC, abstractmethod
from app.core.entities.client import Client


class ClientRepositoryInterface(ABC):

    @abstractmethod
    def add(self, client: Client) -> None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Client | None:
        pass

    @abstractmethod
    def update(self, client: Client) -> None:
        pass

    @abstractmethod
    def delete(self, email: str) -> None:
        pass
