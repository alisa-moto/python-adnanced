"""
Для проекта Библиотека реализовать:
- класс-интерфейс для управления хранилищем (например, load_books, save_books, load_readers, save_readers)
- детализированный класс JSONStorage (загрузка и сохранение книг/читателей в БД)
"""

from abc import ABC, abstractmethod

from HW_06.units.book import Book
from HW_06.units.reader import Reader


class BaseDB(ABC):
    @abstractmethod
    def load_books_from_db(self) -> list:
        pass

    @abstractmethod
    def load_books_from_db_by_input(self, **kwargs):
        pass

    @abstractmethod
    def save_books_to_db(self, books_obj: list):
        pass

    @abstractmethod
    def load_readers_from_db(self) -> list:
        pass

    @abstractmethod
    def load_reader_from_db_by_input(self, **kwargs):
        pass

    @abstractmethod
    def save_readers_to_db(self, readers_obj: list):
        pass

    @abstractmethod
    def add_book_to_db(self, books_obj: Book) -> bool:
        pass

    @abstractmethod
    def delete_book_from_db(self, books_obj: Book) -> bool:
        pass

    @abstractmethod
    def add_reader_to_db(self, reader_obj: Reader) -> bool:
        pass

    @abstractmethod
    def delete_reader_from_db(self, reader_obj: Reader) -> bool:
        pass

    @abstractmethod
    def change_book_in_db(self, books_obj: Book) -> bool:
        pass

    @abstractmethod
    def change_reader_in_db(self, reader_obj: Reader) -> bool:
        pass
