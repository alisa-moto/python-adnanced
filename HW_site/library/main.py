from flask import Flask, render_template, request

from HW_site.library.data_base.sql_units.sql_data_base import SQLDataBase
from HW_site.library.library import Library
from HW_site.library.units.book import Book
from HW_site.library.units.reader import Reader


app = Flask(__name__, template_folder="../site/templates",
            static_folder="../site/static")

app.config['DEBUG'] = True

storage = SQLDataBase('postgres', 'pass123', 'postgres')


@app.route('/index')
def home_page():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/books', methods=['GET'])
def all_books_page():
    return render_template('books.html', books=sorted(lib.print_all_books(), key=lambda book: book.book_id))


@app.route('/add_book', methods=['GET', 'POST'])
def add_book_page():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')

        if not (title and author and year):
            return render_template('add_book.html', message='You entered an invalid data. Please try again')
        if not year.isnumeric():
            return render_template('add_book.html', message='You entered an invalid publishing year. Please try again')

        ret_msg = lib.add_book_to_library(title, author, int(year))
        return render_template('add_book.html', message=ret_msg)

    return render_template('add_book.html')


@app.route('/delete_book', methods=['GET', 'POST'])
def delete_book_page():
    if request.method == 'POST':
        book_id = request.form.get('book_id')

        if not book_id.isnumeric():
            return render_template('delete_book.html', message='You entered an invalid book id. Please try again')

        ret_msg = lib.delete_book_from_library(int(book_id))
        return render_template('delete_book.html', message=ret_msg)

    return render_template('delete_book.html')


if __name__ == '__main__':
    books = [
        Book('Ring', 'Marek Zorica', 1994),
        Book('Song', 'Anton Iggy', 1984),
        Book('Lullaby', 'Robert B. Wide', 2020),
    ]

    readers = [
        Reader('Mini', 'Driver', 2005),
        Reader('Glen', 'Johnson', 1975),
        Reader('Nina', 'Hagen', 1887),
    ]

    lib = Library(storage, books, readers)
    # print(*lib.print_all_books())
    # print(*lib.print_all_readers())

    app.run()
