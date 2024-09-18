import click
from flask.cli import with_appcontext
from app.infrastructure.seeder.seed_data import seed_all

def register_commands(app):
    @app.cli.command('seed_db')
    @with_appcontext
    def seed_db():
        seed_all()
        click.echo('Database seeded successfully.')
