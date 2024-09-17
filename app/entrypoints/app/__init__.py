from flask import Flask
from dotenv import load_dotenv
import os
from app.core.repositories.client.client_repository import ClientRepository
from app.core.repositories.client.client_repository_interface import ClientRepositoryInterface
from app.infrastructure.config import DevelopmentConfig, ProductionConfig, TestingConfig
from app.infrastructure.extensions import db, jwt, cache
from app.infrastructure.database import init_db
from app.entrypoints.app.routes.client_routes import register_client_routes

load_dotenv()

def create_app():
    app = Flask(__name__)

    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
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

    register_client_routes(app, client_repository)

    return app
