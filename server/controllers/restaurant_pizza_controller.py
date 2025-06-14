from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(rp)
        db.session.commit()

        pizza = Pizza.query.get(pizza_id)
        restaurant = Restaurant.query.get(restaurant_id)

        return jsonify({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": pizza.id,
            "restaurant_id": restaurant.id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        }), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
