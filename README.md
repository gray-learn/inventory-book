# Book Inventory Management System - Backend (Django)

## Overview

This is the backend for the Book Inventory Management System, built using Django and Django REST Framework. It provides APIs for managing books, including adding new books, filtering by criteria, and exporting book data.

## Features

- **CRUD Operations**: Create, read, update, and delete books from the inventory.
- **Filtering**: Filter books based on title, author, genre, and publication date.
- **Export Data**: Export book data in JSON or CSV format.
- **API Integration**: Use Django REST Framework to expose APIs for frontend interaction.
- **Validation**: Input data is validated for correctness (e.g., ISBN format, non-empty fields).

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- Django 4.x
- Django REST Framework

## Project Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/gray-learn/inventory-book.git
   cd book-inventory-backend
   ```

2. **Create a Virtual Environment**

   It's recommended to create a virtual environment to isolate dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   Install all required dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**

   The default database is SQLite. You can use other RDBMS (like PostgreSQL or MySQL) by updating `DATABASES` in `settings.py`.

   Run migrations to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The server will be available at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **Books List**: Retrieve the list of all books.
  - `GET /api/books/`
  
- **Add Book**: Add a new book to the inventory.
  - `POST /api/books/`
  
- **Filter Books**: Filter books by title, author, genre, or publication date.
  - `GET /api/books/?title=example&author=example`
  
- **Update Book**: Update details of a book by its ID.
  - `PUT /api/books/{id}/`
  
- **Delete Book**: Delete a book by its ID.
  - `DELETE /api/books/{id}/`
  
- **Export Data**: Export all books in CSV or JSON format.
  - `GET /api/books/export/?format=csv` or `GET /api/books/export/?format=json`

## Testing

The project comes with unit tests for views, models, and serializers.

### Run the Test Suite

To run the Django test suite, use the following command:
python manage.py test

### Test Coverage

Ensure that the `tests/` directory contains tests for:
- Models (`tests/test_models.py`)
- Views (`tests/test_views.py`)
- Serializers (`tests/test_serializers.py`)

## Folder Structure
book_inventory_backend/
├── inventory/ # Django app folder
│ ├── migrations/ # Database migration files
│ ├── models.py # Book model definition
│ ├── serializers.py # API serializers
│ ├── views.py # API viewsets
│ ├── urls.py # App-specific URL routing
│ ├── tests/ # Unit tests for the app
│ └── admin.py # Admin panel configuration
├── book_inventory/ # Django project folder
│ ├── settings.py # Project settings
│ ├── urls.py # Project-wide URL routing
│ └── wsgi.py # WSGI entry point for the app
├── manage.py # Django project management command
├── requirements.txt # Python package dependencies
└── README.md # Project documentation

## API Documentation

The API documentation is automatically generated using Django REST Framework's browsable API. Once the server is running, navigate to the base API URL to interact with the API using a web interface:

[http://localhost:8000/api/](http://localhost:8000/api/)
