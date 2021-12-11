import json
import os
from abc import ABC

from HW_06.data_base_pack.base_db import BaseDB
from HW_06.units.book import Book
from HW_06.units.reader import Reader


class JsonDBLoad(BaseDB, ABC):
    def __init__(self, books_json_filename, readers_json_filename):
        self.__books_json_filename = books_json_filename
        self.__readers_json_filename = readers_json_filename

    # common load and save methods
    def load_books_from_db(self):
        """Method to load full Book objects list as reverted from json dictionary"""
        if not os.path.exists(self.__books_json_filename):
            print('There is no json file with books.')
            return []
        with open(self.__books_json_filename) as file:
            dict_with_books = json.load(file)

        return [
            Book.book_from_dict(book)
            for book in dict_with_books
        ]

    def save_books_to_db(self, books_obj: list):
        """Method to write full Book objects list as dictionary to json file"""
        with open(self.__books_json_filename, 'w') as file:
            json.dump(
                [
                    book.book_to_dict()
                    for book in books_obj
                ], file, indent=1)

    def load_readers_from_db(self):
        """Method to load full Reader objects list as reverted from json dictionary"""
        if not os.path.exists(self.__readers_json_filename):
            print('There is no json file with readers.')
            return []

        with open(self.__readers_json_filename) as file:
            dict_with_readers = json.load(file)

        return [
            Reader.reader_from_dict(reader)
            for reader in dict_with_readers
        ]

    def save_readers_to_db(self, readers_obj: list):
        """Method to write full Reader objects list as dictionary to json file"""
        with open(self.__readers_json_filename, 'w') as file:
            json.dump(
                [
                    reader.reader_to_dict()
                    for reader in readers_obj
                ], file, indent=1)

    # detailed add, delete, update methods
    # TODO: add logic to  the detailed methods
    def add_book_to_db(self, books_obj: Book) -> bool:
        pass

    def delete_book_from_db(self, books_obj: Book) -> bool:
        pass

    def add_reader_to_db(self, reader_obj: Reader) -> bool:
        pass

    def delete_reader_from_db(self, reader_obj: Reader) -> bool:
        pass

    def change_book_in_db(self):
        pass

    def change_reader_in_db(self):
        pass
