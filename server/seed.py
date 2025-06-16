import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

fake = Faker()

with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()
    print("Creating tables...")
    db.create_all()

    #restaurants
    restaurants = []
    for _ in range(10):
        r = Restaurant(name=fake.company(), address=fake.address())
        restaurants.append(r)

    # pizzas
    pizzas = []
    for _ in range(10):
        p = Pizza(name=fake.word().capitalize(), ingredients=", ".join([fake.word() for _ in range(3)]))
        pizzas.append(p)

    db.session.add_all(restaurants + pizzas)
    db.session.commit()

    # restaurant_pizzas with prices
    restaurant_pizzas = []
    for i in range(10):
        rp = RestaurantPizza(
            price=fake.random_int(min=1, max=30),
            pizza_id=pizzas[i].id,
            restaurant_id=restaurants[i].id
        )
        restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Seed complete!")
