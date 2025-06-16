import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

fake = Faker()

# relevant pizza names and ingredients
pizza_data = [
    {"name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil"},
    {"name": "Pepperoni", "ingredients": "Tomato, Mozzarella, Pepperoni"},
    {"name": "BBQ Chicken", "ingredients": "BBQ Sauce, Chicken, Red Onion, Cilantro"},
    {"name": "Hawaiian", "ingredients": "Tomato, Mozzarella, Ham, Pineapple"},
    {"name": "Veggie", "ingredients": "Tomato, Mozzarella, Bell Peppers, Olives, Onions"},
    {"name": "Meat Lovers", "ingredients": "Tomato, Mozzarella, Sausage, Bacon, Pepperoni"},
    {"name": "Four Cheese", "ingredients": "Mozzarella, Parmesan, Gorgonzola, Ricotta"},
    {"name": "Buffalo Chicken", "ingredients": "Buffalo Sauce, Chicken, Mozzarella, Blue Cheese"},
    {"name": "Supreme", "ingredients": "Tomato, Mozzarella, Pepperoni, Sausage, Bell Peppers, Onions"},
    {"name": "Mediterranean", "ingredients": "Tomato, Feta, Olives, Spinach, Red Onion"}
]

# Predefined relevant restaurant names
restaurant_names = [
    "Papa's Pizzeria",
    "The Pizza Oven",
    "Slice of Heaven",
    "The Italian Pie",
    "Crust & Craft",
    "Dough Bros",
    "The Saucy Slice",
    "Bella's Pizza",
    "Firebrick Pies",
    "The Rolling Dough"
]

with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()
    print("Creating tables...")
    db.create_all()

    # Create restaurants
    restaurants = []
    for name in restaurant_names:
        r = Restaurant(name=name, address=fake.address())
        restaurants.append(r)

    # Create pizzas
    pizzas = []
    for p in pizza_data:
        pizza = Pizza(name=p["name"], ingredients=p["ingredients"])
        pizzas.append(pizza)

    db.session.add_all(restaurants + pizzas)
    db.session.commit()

    # Create restaurant_pizzas with prices 
    restaurant_pizzas = []
    for i in range(len(pizzas)):
        rp = RestaurantPizza(
            price=fake.random_int(min=1, max=30),
            pizza_id=pizzas[i].id,
            restaurant_id=restaurants[i].id
        )
        restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Seed complete!")
