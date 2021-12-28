from HW_08.server.library.data_base_pack.base_db import BaseDB
from HW_08.server.library.units.book import Book
from HW_08.server.library.units.reader import Reader
"""
The module for the library with readers and books lists in it
"""


class Library:
    def __init__(self, storage: BaseDB,
                 books_list: list = None,
                 readers_list: list = None) -> None:
        self.__storage = storage

        self.__books_list = books_list if books_list else []
        self.__readers_list = readers_list if readers_list else []

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

    def add_book_to_library(self, book_name, book_author, book_date) -> str:
        """
        Method adds book to library list with user's input of book_name, book_author, book_date. Book_id is a random
        unique int, book_id_reader is None by default
        Save a new book to a json file
        :return:
        str with data of added book
        """
        book = Book(book_name, book_author, book_date)
        self.__books_list.append(book)
        self.save_books()
        return f'Book {book} is added to library.'

    def delete_book_from_library(self) -> str:
        """
        Method deletes book from library list with user's book_id input
        Delete a book from a json file
        :return:
        str with data of deleted book
        """
        book_id = input("Please enter book id: ")
        book = self.__get_book_by_id(int(book_id))
        if not book:
            return f'There is no book with id = {book_id}'
        else:
            self.__books_list.remove(book)
            self.save_books()
            return f'Book {book} is deleted from library.'

    def create_reader(self, first_name: str, last_name, birth_year) -> str:
        """
        Method adds reader to library list with user's input of first_name, last_name, birth_year. Reader_id is a random
        unique int, reader_book_id is None by default
        Save a new reader to a json file
        :return:
        str with data of added reader
        """
        reader = Reader(first_name, last_name, birth_year)
        self.__readers_list.append(reader)
        self.save_readers()
        return f'Reader {reader} is successfully created.'

    def delete_reader(self) -> str:
        """
        Method deletes reader from library list with user's reader_id input
        Delete a reader from a json file
        :return:
        str with data of deleted reader
        """
        reader_id = input("Please enter reader id: ")
        reader = self.__get_reader_by_id(int(reader_id))
        if not reader:
            return f'There is no reader with id = {reader_id}'
        else:
            self.__readers_list.remove(reader)
            self.save_readers()
            return f'Reader {reader} is successfully deleted.'

    def print_all_books(self):
        """
        Method prints all books in library book list
        :return:
        """
        for book in self.__books_list:
            print(book)

    def print_books_in_library(self):
        """
        Method prints all available for readers books in library book list by checking book_id_reader: if it's None
        book is available
        :return:
        """
        for book in self.__books_list:
            if book.get_book_id_reader() is None:
                print(book)

    def print_taken_books(self):
        """
        Method prints all taken by readers books in library book list by checking book_id_reader: if it's not None
        book is not available
        :return:
        """
        for book in self.__books_list:
            if book.get_book_id_reader() is not None:
                print(book)

    def print_all_readers(self):
        """
        Method prints all readers in library readers list
        :return:
        """
        for reader in self.__readers_list:
            print(reader)

    def print_readers_with_book(self):
        """
        Method prints all readers with taken books in library readers list by checking reader_book_id: if it's not None
        reader has at least one book
        :return:
        """
        for reader in self.__readers_list:
            if reader.get_reader_book_id() is not None:
                print(reader)

    def give_book_to_reader(self, book_id: int, reader_id: int) -> str:
        """
        Method gives book to reader by changing book_id_reader parameter of book object to actual reader_id and
        reader_book_id of reader object to actual book_id
        :param book_id: int, is get from ask_for_ids method input
        :param reader_id: int, is get from ask_for_ids method input
        :return: str with ids of book and reader
        """
        book = self.__get_book_by_id(book_id)
        if not book:
            return f'Error: book with id {book_id} is not found.'

        reader = self.__get_reader_by_id(reader_id)
        if not reader:
            return f'Error: reader with id {reader_id} is not found.'

        if book.get_book_id_reader() is not None:
            return f'The book with id {book_id} has already been taken.'

        book.set_book_id_reader(reader_id)
        reader.set_reader_book_id(book_id)
        return f'Book with id {book_id} was given to reader with id {reader_id}.'

    def take_book_from_reader(self, book_id: int, reader_id: int) -> str:
        """
        Method takes book from reader by changing book_id_reader parameter of book object to None and
        reader_book_id of reader object to None
        :param book_id: int, is get from ask_for_ids method input
        :param reader_id: int, is get from ask_for_ids method input
        :return: str with ids of book and reader
        """
        book = self.__get_book_by_id(book_id)
        if not book:
            return f'Error: book with id {book_id} is not found.'

        reader = self.__get_reader_by_id(reader_id)
        if not reader:
            return f'Error: reader with id {reader_id} is not found.'

        if book.get_book_id_reader() is None:
            return f'The book with id {book_id} is not taken.'

        book.set_book_id_reader(None)
        reader.set_reader_book_id(None)
        return f'Book with id {book_id} was taken back from reader with id {reader_id}.'

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
