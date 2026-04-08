## E-commerce Store
 
## Features: 
- Product catalog with hierarchical categories
- Cart & order system with atomic transactions
- Custom user model 
- Comment system with moderation
- REST API with token auth
- Admin panel customizations

## Tech-Stack:
- Python
- Django & Django REST Framework
- PostgreSQL
- Linux (WSL2)
- Docker & Docker Compose

## Requirements
- Python 
- Django
- PostgreSQL
- Docker, Docker Compose
- Suggestion: Linux/WSL 2 

## How to run

  1. Clone repository
  git clone https://github.com/NikitaDid/ecommerce-store
  cd ecommerce-store

  2. Start the project
  docker-compose up --build
  
  3. Open in browser
  http://localhost:8080

  4. Stop the project
  docker-compose down

## Environment Variables

This project requires a `.env` file in the root directory.
The `.env` file is not included in the repository for security reasons.

Create a `.env` file and add the following variables:

- DJANGO_SECRET_KEY=your_secret_key
- DJANGO_DEBUG=True
- POSTGRES_USER=your_user
- POSTGRES_PASSWORD=your_password
- POSTGRES_DB=your_database
- DB_NAME=your_database
- DB_USER=your_user
- DB_PASSWORD=your_password
- DB_HOST=127.0.0.1
- DB_PORT=5432
  
## Author
Mykyta 
