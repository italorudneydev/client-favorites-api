from app.infrastructure.extensions import db
from app.infrastructure.seeder.seed_data import seed_all

def init_db(app):
    with app.app_context():
        db.create_all()
        seed_all()
