from itertools import product

from flask import Flask
from dotenv import load_dotenv
import os
from app.core.repositories.client_repository import ClientRepository
from app.core.repositories.client_repository_interface import ClientRepositoryInterface
from app.core.repositories.product_repository import ProductRepository
from app.core.repositories.product_repository_interface import ProductRepositoryInterface
from app.infrastructure.config import DevelopmentConfig, ProductionConfig, TestingConfig
from app.infrastructure.extensions import db, jwt, cache
from app.infrastructure.database import init_db
from app.entrypoints.app.routes.client_routes import register_client_routes
from app.entrypoints.app.routes.client_favorite_products_routes import register_client_favorite_products_routes

load_dotenv()

def create_app(config_name=os.getenv('FLASK_ENV', 'development')):
    app = Flask(__name__)

    if config_name == 'production':
        app.config.from_object(ProductionConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    init_db(app)
    jwt.init_app(app)
    cache.init_app(app)

    with app.app_context():
        session = db.session

    client_repository: ClientRepositoryInterface = ClientRepository(session)
    product_repository: ProductRepositoryInterface = ProductRepository(session)

    register_client_favorite_products_routes(app, client_repository, product_repository)
    register_client_routes(app, client_repository)

    return app
