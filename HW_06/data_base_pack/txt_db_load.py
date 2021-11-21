from HW_06.data_base_pack.base_db import BaseDB

from HW_06.units.book import Book
from HW_06.units.reader import Reader

# TODO release this class as JSON one


class TxtDBLoad(BaseDB):
    def load_books_from_db(self) -> list:
        pass

    def save_books_to_db(self, books_obj: list):
        pass

    def load_readers_from_db(self) -> list:
        pass

    def save_readers_to_db(self, readers_obj: list):
        pass

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
