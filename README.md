# Pizza API Challenge

## Setup Instructions

1. Install dependencies using pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```

2. Set environment variables as needed (e.g., `FLASK_APP=server/app.py`).

3. Run the Flask development server:
   ```bash
   flask run
   ```

## Database Migration & Seeding

- To generate a new migration after model changes:
  ```bash
  alembic -c migrations/alembic.ini revision --autogenerate -m "Migration message"
  ```

- To apply migrations to the database:
  ```bash
  alembic -c migrations/alembic.ini upgrade head
  ```

- To seed the database with initial data:
  ```bash
  python server/seed.py
  ```

## Route Summary

- `GET /restaurants` - List all restaurants
- `GET /restaurants/<id>` - Get a specific restaurant
- `POST /restaurants` - Create a new restaurant
- `DELETE /restaurants/<id>` - Delete a restaurant (cascades to restaurant_pizzas)
- `GET /pizzas` - List all pizzas
- `GET /pizzas/<id>` - Get a specific pizza
- `POST /pizzas` - Create a new pizza
- `GET /restaurant_pizzas` - List all restaurant pizzas
- `POST /restaurant_pizzas` - Create a new restaurant pizza (with price validation)
- `DELETE /restaurant_pizzas/<id>` - Delete a restaurant pizza

## Example Requests & Responses

### Create RestaurantPizza

Request:
```json
POST /restaurant_pizzas
{
  "price": 15,
  "restaurant_id": 1,
  "pizza_id": 2
}
```

Response:
```json
{
  "id": 1,
  "price": 15,
  "restaurant_id": 1,
  "pizza_id": 2
}
```

### Validation Rules

- `price` in `restaurant_pizzas` must be an integer between 1 and 30.
- Cascading deletes: Deleting a restaurant deletes associated restaurant_pizzas.

## Postman Usage

- Import the provided `challenge-1-pizzas.postman_collection.json` into Postman.
- Use the collection to test all API endpoints with example requests.

