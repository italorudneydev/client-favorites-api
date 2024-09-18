from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_caching import Cache

db = SQLAlchemy()
jwt = JWTManager()
cache = Cache(config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://luiza_cache:6379/0'})
