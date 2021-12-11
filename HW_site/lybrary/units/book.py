"""
The module for the item "Book"
"""


class Book:
    """Class to create book in library with unique parameter book_id to each item"""
    def __init__(self, book_name: str, book_author: str, book_date: int, book_id_reader=None):
        self.__book_id = int(id(self))
        self.__book_name = book_name
        self.__book_author = book_author
        self.__book_date = book_date
        """Change book_id_reader to a reader's id if book is being taken by this reader. 
        None if book is in the library."""
        self.__book_id_reader = book_id_reader

    def __str__(self):
        return f'{self.__book_id}: {self.__book_name}, {self.__book_author}, {self.__book_date}, ' \
               f'{self.__book_id_reader}'

    def get_book_id(self) -> int:
        return self.__book_id

    def get_book_name(self) -> str:
        return self.__book_name

    def get_book_author(self) -> str:
        return self.__book_author

    def get_book_date(self) -> int:
        return self.__book_date

    def get_book_id_reader(self) -> int:
        return self.__book_id_reader

    def set_book_id_reader(self, book_id_reader: int) -> None:
        self.__book_id_reader = book_id_reader
