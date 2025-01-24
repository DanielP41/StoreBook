# Book Store

## Description

StoreBook is a web application developed with Flask that allows users to manage books and authors. Users can add, edit, delete and search for books and authors.

## Project Structure

The structure of the project is as follows:

book_store/
│
├── app/
│   ├── __init__.py             # Initializes the Flask application and settings
│   ├── models.py               # Defines the database models
│   ├── routes.py               # Defines the routes and logic of the application
│   ├── templates/              # Folder containing HTML templates
│   │   ├── index.html          # Template for home page
│   │   ├── books.html          # Template for book list
│   │   ├── edit_book.html      # Template for editing a book
│   │   ├── authors.html        # Template for the list of authors
│   │   └── search_results.html # Template for search results
│
├── venv/                       # Python virtual environment
├── run.py                      # Script to start the Flask application
├── requirements.txt            # Dependency archiving
└── README.md                   # Project documentation
