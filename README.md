# Microservices Product Management System with Django, Flask, and React

A microservices-based application demonstrating a product management system. This system is composed of three main services:

- Django Microservice: Manages CRUD operations for products.
- Flask Microservice: Lists products from the Django service and handles product likes.
- React Frontend: Provides a user interface for interacting with the products.
- RabbitMQ is used for messaging between services, ensuring loose coupling and event-driven updates.


## Getting Started

### Installing
1. Clone the repository:

```bash
git clone https://github.com/amine-el-amrani/python_microservices_web_app.git
cd python_microservices_web_app.git
```

2. Start Django service

```bash
cd admin
docker compose build
docker compose up -d
```

3. Start Flask service

```bash
cd main
docker compose build
docker compose up -d
```

4. Set up the React frontend:

```bash
cd react-crud-main
npm install
npm start
```

## Authors
EL AMRANI Amine
