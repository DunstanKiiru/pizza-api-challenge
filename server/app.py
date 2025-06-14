from flask import Flask
from flask_migrate import Migrate
from models import db
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route("/")
def index():
    return {"message": "Pizza Restaurant API is live!"}
