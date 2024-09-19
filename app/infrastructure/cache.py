from app.core.interfaces.cache_interface import CacheInterface
from app.infrastructure.extensions import cache

class RedisCache(CacheInterface):
    def get(self, key: str):
        return cache.get(key)

    def set(self, key: str, value, timeout: int = 300):
        cache.set(key, value, timeout=timeout)

    def delete(self, key: str):
        cache.delete(key)