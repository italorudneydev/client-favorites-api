import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    CACHE_REDIS_HOST = os.getenv('CACHE_REDIS_HOST')
    CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL')
    CACHE_REDIS_PORT = int(os.getenv('CACHE_REDIS_PORT', 6379))

class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'

class ProductionConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
