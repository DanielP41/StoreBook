from flask import Flask, render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Author, Book

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para listar y agregar libros
@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']
        if len(title) < 3 or author_id == "":
            flash("Por favor, ingresa un título válido y selecciona un autor.")
        else:
            book = Book(title=title, author_id=author_id)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('books'))
    
    books = Book.query.all()
    authors = Author.query.all()
    return render_template('books.html', books=books, authors=authors)

# **Ruta para editar libros**
@app.route('/books/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author_id = request.form['author_id']
        db.session.commit()
        return redirect(url_for('books'))
    authors = Author.query.all()
    return render_template('edit_book.html', book=book, authors=authors)

# **Ruta authors**
@app.route('/authors', methods=['GET', 'POST'])
def authors():
    if request.method == 'POST':
        name = request.form['name']
        if len(name) < 1:
            flash("Por favor, ingresa un nombre válido para el autor.")
        else:
            author = Author(name=name)
            db.session.add(author)
            db.session.commit()
            return redirect(url_for('authors'))
    
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)
