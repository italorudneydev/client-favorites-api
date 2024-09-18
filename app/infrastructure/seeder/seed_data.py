from faker import Faker
from app.infrastructure.extensions import db
from app.core.entities.product import Product

fake = Faker()


def seed_products(num_products=500):
    for _ in range(num_products):
        product = Product(
            title=fake.word(),
            price=fake.pyfloat(left_digits=None, right_digits=2, positive=True),
            image=fake.image_url(),
            brand=fake.company(),
            review_score=fake.pydecimal(left_digits=1, right_digits=1, positive=True)
        )
        db.session.add(product)
    db.session.commit()

def seed_all():
    seed_products()

