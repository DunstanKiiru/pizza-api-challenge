import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
from server.app import app
from server.models import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

fake = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    # restaurants
    r1 = Restaurant(name=fake.company(), address=fake.address())
    r2 = Restaurant(name=fake.company(), address=fake.address())

    # fake pizzas
    p1 = Pizza(name=fake.word().capitalize(), ingredients=", ".join([fake.word() for _ in range(3)]))
    p2 = Pizza(name=fake.word().capitalize(), ingredients=", ".join([fake.word() for _ in range(3)]))

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    # restaurant pizza prices
    rp1 = RestaurantPizza(price=fake.random_int(min=5, max=20), pizza_id=p1.id, restaurant_id=r1.id)
    rp2 = RestaurantPizza(price=fake.random_int(min=5, max=20), pizza_id=p2.id, restaurant_id=r2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print("Seed complete!")
