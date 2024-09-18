from abc import ABC, abstractmethod

class CacheInterface(ABC):
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value, timeout: int = 300):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass