from HW_site.library.data_base.base_db import BaseDB
from HW_site.library.units.book import Book
from HW_site.library.units.reader import Reader

"""
The module for the library with readers and books lists in it
"""


class Library:
    def __init__(self, storage: BaseDB,
                 books_list: list = None,
                 readers_list: list = None) -> None:
        self.__storage = storage

        if books_list:
            self.__storage.save_books_to_db(books_list)

        if readers_list:
            self.__storage.save_readers_to_db(readers_list)

    def __get_book_by_id(self, _book_id: int):
        for book in self.__books_list:
            if book.get_book_id() == _book_id:
                return book
        else:
            return None

    def __get_reader_by_id(self, _reader_id: int):
        for reader in self.__readers_list:
            if reader.get_reader_id() == _reader_id:
                return reader
        else:
            return None

    @staticmethod
    def ask_for_ids():
        """
        Method asks user for book_id and reader_id, checks if there are a valid positive integers
        :return:
        book_id -> int
        reader_id -> int
        """
        while True:
            book_id, reader_id = input("Please enter book id and reader id split by comma: ").split(',')
            if book_id.isdigit() and reader_id.isdigit():
                return int(book_id), int(reader_id)
            else:
                print("You have entered not a valid positive integers as ids.")

    @staticmethod
    def ask_for_book_params():
        """
        Method asks user for book_name, book_author, book_date and validate that user entered all these parameters
        :return:
        book_name -> str
        book_author -> str
        book_date -> int
        """
        while True:
            try:
                book_name, book_author, book_date = input("Please enter title, author name, year of edition "
                                                          "split by comma as in the example 'River,Anthony Bach,"
                                                          "1956': ").split(',')
                return str(book_name), str(book_author), int(book_date)
            except ValueError:
                print("Could you check your input is as an example 'River,Anthony Bach,1956' and try to enter book "
                      "parameters again.")

    @staticmethod
    def ask_for_reader_params():
        """
        Method asks user for first_name, last_name, birth_year and validate that user entered all these parameters
        :return:
        first_name -> str
        last_name -> str
        birth_year -> int
        """
        while True:
            try:
                first_name, last_name, birth_year = input("Please enter first name, last name, birth "
                                                          "year split by comma as in the example 'Linn,Lindon,"
                                                          "1997': ").split(',')
                return str(first_name), str(last_name), int(birth_year)
            except ValueError:
                print("Could you check your input is as an example 'Linn,Lindon,,1997' and try to enter reader "
                      "parameters again.")

    def add_book_to_library(self, book_name: str, book_author: str, book_date: int) -> str:
        """
        Method adds book to library list with user's input of book_name, book_author, book_date. Book_id is a random
        unique int, book_id_reader is None by default
        Save a new book to a json file
        :return:
        str with data of added book
        """
        book = Book(book_name, book_author, book_date)
        if self.__storage.add_book_to_db(book):
            result_message = f'Book {book.book_name} with id={book.book_id} is added to library.'
            return result_message
        else:
            return 'Error: your book was not saved!'

    def delete_book_from_library(self, temp_id: int) -> str:
        """
        Method deletes book from library list with user's book_id input
        Delete a book from a json file
        :return:
        str with data of deleted book
        """
        book = self.__storage.load_books_from_db_by_input(temp_id=temp_id)
        if not book:
            return f'There is no book with id = {temp_id}'

        book = book[0]

        self.__storage.delete_book_from_db(book)
        result_message = f'Book {book.book_name} with id={book.book_id} is deleted from library.'
        return result_message

    def create_reader(self, first_name: str, last_name, birth_year) -> str:
        """
        Method adds reader to library list with user's input of first_name, last_name, birth_year. Reader_id is a random
        unique int, reader_book_id is None by default
        Save a new reader to a json file
        :return:
        str with data of added reader
        """
        reader = Reader(first_name, last_name, birth_year)
        if self.__storage.add_reader_to_db(reader):
            result_message = f'Reader {reader.first_name} {reader.last_name} with id={reader.reader_id} ' \
                             f'is successfully created.'
            return result_message
        else:
            return 'Error: the reader was not saved!'

    def delete_reader(self, temp_id) -> str:
        """
        Method deletes reader from library list with user's reader_id input
        Delete a reader from a json file
        :return:
        str with data of deleted reader
        """
        reader = self.__storage.load_books_from_db_by_input(temp_id=temp_id)
        if not reader:
            return f'There is no reader with id = {temp_id}'

        reader = reader[0]

        self.__storage.delete_reader_from_db(reader)
        result_message = f'Reader {reader.first_name} {reader.last_name} with id={reader.reader_id}' \
                         f' is deleted from library.'
        return result_message

    def print_all_books(self):
        """
        Method prints all books in library book list
        :return:
        """
        return self.__storage.load_books_from_db()

    def print_books_in_library(self):
        """
        Method prints all available for readers books in library book list by checking book_id_reader: if it's None
        book is available
        :return:
        """
        return [temp_book for temp_book in self.__storage.load_books_from_db() if not temp_book.get_book_id_reader()]

    def print_taken_books(self):
        """
        Method prints all taken by readers books in library book list by checking book_id_reader: if it's not None
        book is not available
        :return:
        """
        return [temp_book for temp_book in self.__storage.load_books_from_db() if temp_book.get_book_id_reader()]

    def print_all_readers(self):
        """
        Method prints all readers in library readers list
        :return:
        """
        return self.__storage.load_readers_from_db()

    def print_readers_with_book(self):
        """
        Method prints all readers with taken books in library readers list by checking reader_book_id: if it's not None
        reader has at least one book
        :return:
        """
        return [temp_reader for temp_reader in self.__storage.load_readers_from_db() if not temp_reader.get_reader_book_id()]

    def give_book_to_reader(self, book_id: int, reader_id: int) -> str:
        """
        Method gives book to reader by changing book_id_reader parameter of book object to actual reader_id and
        reader_book_id of reader object to actual book_id
        :param book_id: int, is get from ask_for_ids method input
        :param reader_id: int, is get from ask_for_ids method input
        :return: str with ids of book and reader
        """

        result_message = ''

        book = self.__storage.load_books_from_db_by_input(book_id=book_id)
        if not book:
            result_message = f'Error: book with id {book_id} is not found.'
            return result_message

        book = book[0]

        if not book.get_book_id_reader():
            result_message = f'The book with id {book_id} has already been taken.'
            return result_message

        reader = self.__storage.load_readers_from_db_by_input(reader_id=reader_id)
        if not reader:
            result_message = f'Error: reader with id {reader_id} is not found.'
            return result_message

        reader = reader[0]

        book.set_book_id_reader(reader_id)
        reader.set_reader_book_id(book_id)
        self.__storage.change_book_in_db(book)
        self.__storage.change_reader_in_db(reader)
        result_message = f'Book with id {book_id} was given to reader with id {reader_id}.'
        return result_message

    def take_book_from_reader(self, book_id: int, reader_id: int) -> str:
        """
        Method takes book from reader by changing book_id_reader parameter of book object to None and
        reader_book_id of reader object to None
        :param book_id: int, is get from ask_for_ids method input
        :param reader_id: int, is get from ask_for_ids method input
        :return: str with ids of book and reader
        """
        result_message = ''

        book = self.__storage.load_books_from_db_by_input(book_id=book_id)
        if not book:
            result_message = f'Error: book with id {book_id} is not found.'
            return result_message

        book = book[0]

        if not book.get_book_id_reader():
            result_message = f'The book with id {book_id} is not taken.'
            return result_message

        reader = self.__storage.load_readers_from_db_by_input(reader_id=reader_id)
        if not reader:
            result_message = f'Error: reader with id {reader_id} is not found.'
            return result_message

        reader = reader[0]

        if book.get_book_id_reader() != reader.get_reader_id():
            result_message = f'Error: reader {reader.reader_first_name} {reader.reader_last_name} has not' \
                             f' taken book with id {book_id}.'
            return result_message

        book.set_book_id_reader(None)
        reader.set_reader_book_id(None)
        self.__storage.change_book_in_db(book)
        self.__storage.change_reader_in_db(reader)
        result_message = f'Book with id {book.book_name} was taken back from ' \
                         f'reader {reader.reader_first_name} {reader.reader_last_name}.'
        return result_message

    def sort_books_by_name(self):
        for book in sorted(self.__books_list, key=lambda x: x.get_book_name()):
            print(book)

    def sort_books_by_author(self):
        for book in sorted(self.__books_list, key=lambda x: x.get_book_author()):
            print(book)

    def sort_books_by_date(self):
        for book in sorted(self.__books_list, key=lambda x: x.get_book_date()):
            print(book)

    def sort_reader_by_first_name(self):
        for reader in sorted(self.__readers_list, key=lambda x: x.get_reader_first_name()):
            print(reader)

    def sort_reader_by_last_name(self):
        for reader in sorted(self.__readers_list, key=lambda x: x.get_reader_last_name()):
            print(reader)

    def sort_reader_by_birth_year(self):
        for reader in sorted(self.__readers_list, key=lambda x: x.get_birth_year()):
            print(reader)

    # Additional methods for books, readers save and load from json files
    def save_books(self):
        """Method takes storage object with json filenames and update book list and/or create file"""
        self.__storage.save_books_to_db(self.__books_list)

    def save_readers(self):
        """Method takes storage object with json filenames and update reader list and/or create json file"""
        self.__storage.save_readers_to_db(self.__readers_list)

    def load_books(self):
        """Method takes storage object with json filenames and return book objects from dict"""
        for book in self.__storage.load_books_from_db():
            print(book)

    def load_readers(self):
        """Method takes storage object with json filenames and return reader objects from dict"""
        for reader in self.__storage.load_readers_from_db():
            print(reader)
