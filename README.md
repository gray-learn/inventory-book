# Book Inventory Management System

## Overview
This project is a Book Inventory Management System built using Django (for the backend) and Vue.js (for the frontend). The system allows users to manage a collection of books, including adding new books, filtering by criteria, and exporting book data in CSV or JSON format.

## Features
- CRUD Operations: Create, read, update, and delete books from the inventory.
- Filtering: Filter books based on title, author, genre, and publication date.
- Export Data: Export book data in JSON or CSV format.
- API Integration: The Vue.js frontend interacts with Django REST Framework APIs to perform CRUD operations.
- Validation: Input data is validated for correctness (e.g., ISBN format, non-empty fields).
- Responsive UI: The frontend is designed to be mobile-friendly and works well on different screen sizes.

## Prerequisites
Before running the project, ensure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- Node.js and npm
- Django 4.x
- Django REST Framework
- Vue.js (Vue CLI)

## Backend Setup (Django)

### 1. Clone the Backend Repository
```bash
git clone https://github.com/gray-learn/inventory-book.git
cd book-inventory-backend
```

### 2. Create a Virtual Environment
It's recommended to create a virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install all required dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Database Setup
The default database is SQLite. You can use other RDBMS (like PostgreSQL or MySQL) by updating DATABASES in settings.py.

Run migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

The server will be available at http://localhost:8000.

## Frontend Setup (Vue.js)
1. Clone the Frontend Repository
```bash
git clone https://github.com/your-repo/book-inventory-frontend.git
cd book-inventory-frontend
```
2. Install Dependencies
```bash
npm install
```
3. Set up Environment Variables
You need to configure API URLs for the Django backend in a .env file or in the axios configuration within the Vue components.

Example .env file:

```bash
VUE_APP_API_BASE_URL=http://localhost:8000/api
```
4. Run the Vue.js Application
```bash
npm run serve
```

The app will now be running at http://localhost:8080.

## Folder Structure

### Backend Folder Structure                # Vue.js project configuration
/book_inventory_backend/
├── inventory/                 # Django app folder
│   ├── migrations/            # Database migration files
│   ├── models.py              # Book model definition
│   ├── serializers.py         # API serializers
│   ├── views.py               # API viewsets
│   ├── urls.py                # App-specific URL routing
│   ├── tests/                 # Unit tests for the app
│   └── admin.py               # Admin panel configuration
├── book_inventory/            # Django project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project-wide URL routing
│   └── wsgi.py                # WSGI entry point for the app
├── manage.py                  # Django project management command
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation

### Frontend Folder Structure
/book-inventory-frontend
├── /src
│   ├── /assets                # Static assets (CSS, images, etc.)
│   ├── /components
│   │   ├── BookForm.vue        # Component for adding new books
│   │   ├── BookList.vue        # Component for displaying the list of books
│   │   └── BookFilter.vue      # Component for filtering books
│   ├── App.vue                # Main component combining the form, list, and filter
│   ├── main.js                # Entry point for Vue.js application
│   ├── router.js              # Optional: If using Vue Router for navigation
├── /public
│   ├── index.html             # Main HTML template
├── /tests                     # Unit and integration tests for Vue components
│   ├── BookForm.spec.js       # Test for BookForm.vue
│   ├── BookList.spec.js       # Test for BookList.vue
│   └── BookFilter.spec.js     # Test for BookFilter.vue
├── package.json               # Project dependencies and scripts
├── README.md                  # This file
└── vue.config.js              # Vue.js project configuration


## API Endpoints
Backend API Endpoints
Books List: Retrieve the list of all books.
GET /api/books/
Add Book: Add a new book to the inventory.
POST /api/books/
Filter Books: Filter books by title, author, genre, or publication date.
GET /api/books/?title=example&author=example
Update Book: Update details of a book by its ID.
PUT /api/books/{id}/
Delete Book: Delete a book by its ID.
DELETE /api/books/{id}/
Export Data: Export all books in CSV or JSON format.
GET /api/books/export/?format=csv or GET /api/books/export/?format=json

## Testing
Backend Testing
To run the Django test suite:

```bash
python manage.py test
```
Make sure that the tests/ directory contains tests for:

Models (tests/test_models.py)
Views (tests/test_views.py)
Serializers (tests/test_serializers.py)

Frontend Testing
To run the tests for Vue components:

```bash
npm run test:unit
```
Tests are located in the /tests directory and cover components like BookForm.vue, BookList.vue, and BookFilter.vue.

## Future Enhancements
Pagination: For larger datasets, consider adding pagination to the book list.
User Authentication: Implement user authentication and authorization for managing books.
Frontend Framework: Consider integrating a frontend framework like Vuetify or Bootstrap to enhance the UI.
Error Handling: Improve error handling both on the frontend and backend for better user feedback.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. Make sure your code follows the existing style and includes tests for any new functionality.

