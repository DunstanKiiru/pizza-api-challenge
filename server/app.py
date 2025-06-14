from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

from .models import db
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_bp
from .controllers.restaurant_pizza_controller import restaurant_pizza_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
