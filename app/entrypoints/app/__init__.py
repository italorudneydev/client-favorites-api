from flask import Flask
from dotenv import load_dotenv
import os
from app.infrastructure.config import DevelopmentConfig, ProductionConfig, TestingConfig
from app.infrastructure.extensions import db, jwt, cache
from app.entrypoints.app.routes import register_routes

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
    jwt.init_app(app)
    cache.init_app(app)

    register_routes(app)

    return app