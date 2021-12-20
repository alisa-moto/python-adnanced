from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, logout_user, current_user, login_required, login_user

from email_validator import validate_email

from HW_site.library.data_base.sql_units.sql_data_base import SQLDataBase
from HW_site.library.library import Library
from HW_site.library.units.book import Book
from HW_site.library.units.reader import Reader

app = Flask(__name__,
            template_folder="../site/templates",
            static_folder="../site/static")

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'My secret key'

login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

storage = SQLDataBase('postgres', 'pass123', 'postgres')

CURRENT_USER = 1


@login_manager.user_loader
def load_user(user_id):
    return lib.get_reader_by_id(user_id)


@app.route('/index')
def home_page():
    return render_template('index.html')


@app.route('/books', methods=['GET'])
@login_required
def all_books_page():
    return render_template('books.html', books=sorted(lib.print_all_books(), key=lambda book: book.book_id))


@app.route('/add_book', methods=['GET', 'POST'])
@login_required
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
@login_required
def delete_book_page():
    if request.method == 'POST':
        book_id = [int(i) for i in request.form.keys() if i.isnumeric()]

        if len(book_id):
            result_message = lib.delete_books_from_library(book_id)
            return render_template('delete_book.html',
                                   books=sorted(lib.print_all_books(), key=lambda book: book.book_id),
                                   message=result_message)

    return render_template('delete_book.html',
                           books=sorted(lib.print_all_books(), key=lambda book: book.book_id))


@app.route('/take_book', methods=['GET', 'POST'])
@login_required
def take_book_page():
    if request.method == 'POST':
        book_id = [int(i) for i in request.form.keys() if i.isnumeric()]

        if len(book_id):
            result_message = lib.give_books_to_reader(book_id, CURRENT_USER)
            return render_template('take_book.html',
                                   books=sorted(lib.print_books_in_library(), key=lambda book: book.book_id),
                                   message=result_message)

    return render_template('take_book.html',
                           books=sorted(lib.print_books_in_library(), key=lambda book: book.book_id))


@app.route('/return_book', methods=['GET', 'POST'])
@login_required
def return_book_page():
    if request.method == 'POST':
        book_id = [int(i) for i in request.form.keys() if i.isnumeric()]

        if len(book_id):
            result_message = lib.take_books_from_reader(book_id, CURRENT_USER)
            return render_template('return_book.html',
                                   books=sorted(lib.show_all_readers_books(CURRENT_USER), key=lambda book: book.book_id),
                                   message=result_message)

    return render_template('return_book.html',
                           books=sorted(lib.show_all_readers_books(CURRENT_USER), key=lambda book: book.book_id))


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up_page():
    if current_user.is_authenticated:
        flash('You have already signed in')
        return redirect(url_for('home_page'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        birth_year = request.form.get('birth_year')

        if not (email and password and first_name and last_name and birth_year):
            flash('Incorrect data. Please try again', 'error')
            return render_template('sign_up.html')
        if not birth_year.isnumeric():
            flash('Incorrect birth year. Please try again', 'error')
            return render_template('sign_up.html')

        try:
            validate_email(email)
        except:
            flash('Incorrect email. Please try again', 'error')
            return render_template('sign_up.html', message='Incorrect email. Please try again')

        if lib.get_reader_by_email(email):
            flash('User with this email already exists', 'error')
            return render_template('sign_up.html', message='User with this email already exists')

        if lib.create_reader(first_name, last_name, birth_year, email, password):
            flash('Your account is successfully created')
            return redirect(url_for('login_page'))
        else:
            flash('Failed attempt to create account. Please try again', 'error')
            return render_template('sign_up.html', message='Failed attempt to create account. Please try again')

    return render_template('sign_up.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if current_user.is_authenticated:
        flash('You have already signed in')
        return redirect(url_for('home_page'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        next_url = request.args.get('next')

        if not (email and password):
            flash('Incorrect data. Please try again', 'error')
            return render_template('login.html')

        reader = lib.get_reader_by_email(email)
        # if reader and reader.check_psw(password):
        if reader:
            login_user(reader)
            if next_url:
                return redirect(next_url)
            return redirect(url_for('home_page'))
        else:
            flash('Invalid email or password', 'error')

    return render_template('login.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout_button():
    logout_user()
    return redirect(url_for('home_page'))


if __name__ == '__main__':
    # books = [
    #     Book('Ring', 'Marek Zorica', 1994),
    #     Book('Song', 'Anton Iggy', 1984),
    #     Book('Lullaby', 'Robert B. Wide', 2020),
    # ]
    #
    # readers = [
    #     Reader('Mini', 'Driver', 2005),
    #     Reader('Glen', 'Johnson', 1975),
    #     Reader('Nina', 'Hagen', 1887),
    # ]

    lib = Library(storage)
    app.run()

    lib.create_reader('test', 'test', 1009, 'moka@test.com', 123)
