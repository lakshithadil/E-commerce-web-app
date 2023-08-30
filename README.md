# E-Commerce Web App Backend with Django
🛒 Back-end with RESTful API end-points for an e-commerce web app using django.

This repository contains the backend code for an e-commerce web app built using Django and Django Rest Framework. The backend provides a set of RESTful API endpoints to manage products, collections, carts, customers, and orders. The app also includes user authentication using JWT web tokens.

## Table of Contents

- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Local Development](#local-development)
- [Authentication](#authentication)
- [Database](#database)
- [Tools Used](#tools-used)
- [Contributing](#contributing)

## Features

- Create, Read, Update, and Delete products, collections, carts, customers, and orders.
- User authentication using JWT web tokens.
- Admin panel to manage app data.
- Utilizes Django ORM for database management.

## API Endpoints

The API provides the following endpoints:

- Products: [GET, POST, PUT, DELETE] `/store/products/`
- Collections: [GET, POST, PUT, DELETE] `/store/collections/`
- Carts: [GET, POST, PUT, DELETE] `/store/carts/`
- Customer: [GET, PUT] `/store/customer/`
- Orders: [GET, POST] `/store/orders/`

Note: we will add full details of the available endpoints future soon.

## Deployment

The web app is deployed on Azure using continuous integration and deployment with GitHub Actions. The deployment process is automated and ensures that the latest code is always deployed to the production environment. 

## Local Development

To run the app locally, follow these steps:

1. Clone this repository.
2. Install virtual environment using `pipenv install`. This will install required dependencies using the pipfile.
3. Activate the virtual environment using `pipenv shell`.
4. Configure your local MySQL database settings in `storefront/settings/dev.py`.
5. Apply migrations using `python manage.py migrate`.
6. Run `python manage.py seed_db` to populate data.
7. Run the development server using `python manage.py runserver`.


## Authentication

User authentication is implemented using JWT web tokens. Users can obtain tokens by logging in. Tokens are required to access protected endpoints. 

## Database

The app uses MySQL as the database. You can find the database schema and models in the `models.py` file. 

## Tools Used

- Python
- Django
- Django Rest Framework
- Djooser (User registration and authentication)
- JWT web tokens
- MySQL (Database)
- Azure (Deployment)
- GitHub Actions (CI/CD)

## Contributing

Contributions are welcome! To contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.


