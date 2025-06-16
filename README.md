# Pizza API Challenge

## Project Overview

This project is a RESTful API for managing restaurants, pizzas, and their relationships. It allows clients to create, read, update, and delete restaurants, pizzas, and restaurant-specific pizza offerings with price validation.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies using pipenv:
   
   ```bash
   pipenv install
   pipenv shell
   ```

3. Set environment variables as needed (e.g., `FLASK_APP=server/app.py`).

4. Run the Flask development server:
   
   ```bash
   flask run
   ```

## Environment Configuration

- Ensure you have Python 3.7+ installed.
- Use pipenv to manage virtual environments and dependencies.
- Configure any necessary environment variables for your setup.

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

## API Route Summary

### Restaurants

- `GET /restaurants` - List all restaurants
- `GET /restaurants/<id>` - Get a specific restaurant by ID
- `POST /restaurants` - Create a new restaurant
- `DELETE /restaurants/<id>` - Delete a restaurant (cascades to restaurant_pizzas)

### Pizzas

- `GET /pizzas` - List all pizzas
- `GET /pizzas/<id>` - Get a specific pizza by ID
- `POST /pizzas` - Create a new pizza

### Restaurant Pizzas

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

## Validation Rules

- `price` in `restaurant_pizzas` must be an integer between 1 and 30.
- Cascading deletes: Deleting a restaurant deletes associated restaurant_pizzas.

## Postman Usage

- Import the provided `challenge-1-pizzas.postman_collection.json` into Postman.
- Use the collection to test all API endpoints with example requests.

## Troubleshooting & Tips

- Ensure your virtual environment is activated before running commands.
- Use Alembic for managing database schema changes.
- Seed the database after migrations to populate initial data.

## Contribution Guidelines

- Fork the repository and create feature branches.
- Write clear commit messages.
- Test your changes thoroughly before submitting pull requests.

## License

This project is open source and licensed under the MIT License that allows reuse within proprietary software provided all copies include the license terms.
