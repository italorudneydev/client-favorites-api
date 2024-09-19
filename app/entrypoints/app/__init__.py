from flask import Flask
from dotenv import load_dotenv
import os
from app.adapters.repositories.client_repository import ClientRepository
from app.adapters.repositories.product_repository import ProductRepository
from app.infrastructure.config import DevelopmentConfig, ProductionConfig, TestingConfig
from app.infrastructure.extensions import db, jwt, cache
from app.infrastructure.cache import RedisCache
from app.infrastructure.database import init_db
from app.entrypoints.app.routes import create_client_bp, create_product_bp

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
        redis_cache = RedisCache()

        client_repository = ClientRepository(session)
        product_repository = ProductRepository(session, redis_cache)

        app.register_blueprint(create_client_bp(client_repository), url_prefix='/api/client')
        app.register_blueprint(create_product_bp(product_repository), url_prefix='/api')
        # app.register_blueprint(create_client_favorite_products_bp(client_repository, product_repository), url_prefix='/api')

    return app
