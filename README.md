# Taskfy

Taskfy is a task management application designed to help users manage their tasks efficiently. It provides features for user authentication, profile management, and task organization. Built with Django and Django REST Framework, Taskfy offers a robust backend API to support task-related operations.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up the Virtual Environment](#set-up-the-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Database Migrations](#database-migrations)
  - [Run the Server](#run-the-server)
- [API Endpoints](#api-endpoints)
  - [User Endpoints](#user-endpoints)
  - [Task Endpoints](#task-endpoints)
- [Models](#models)
  - [Profile](#profile)
  - [Task](#task)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication
- Profile management with image upload
- CRUD operations for tasks
- RESTful API for all operations

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Taskfy.git
cd Taskfy
```

### Set Up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Migrations

Run the following commands to apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.

## API Endpoints

### User Endpoints

- **POST /api/accounts/register/**: Register a new user
- **POST /api/accounts/login/**: Log in a user
- **GET /api/accounts/profile/**: Retrieve profile details
- **PUT /api/accounts/profile/**: Update profile details

### Task Endpoints

- **GET /api/tasks/**: List all tasks
- **POST /api/tasks/**: Create a new task
- **GET /api/tasks/{id}/**: Retrieve a specific task
- **PUT /api/tasks/{id}/**: Update a specific task
- **DELETE /api/tasks/{id}/**: Delete a specific task

