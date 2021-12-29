"""
Для проекта Библиотека реализовать:
- класс-интерфейс для управления хранилищем (например, load_books, save_books, load_readers, save_readers)
- детализированный класс JSONStorage (загрузка и сохранение книг/читателей в БД)
"""

from abc import ABC, abstractmethod

from HW_12.units.book import Book
from HW_12.units.reader import Reader


class BaseDB(ABC):
    @abstractmethod
    def load_books_from_db(self) -> list:
        pass

    @abstractmethod
    def load_books_from_db_by_input(self, **kwargs) -> None:
        pass

    @abstractmethod
    def save_books_to_db(self, books_obj: list) -> None:
        pass

    @abstractmethod
    def load_readers_from_db(self) -> list:
        pass

    @abstractmethod
    def load_reader_from_db_by_input(self, **kwargs) -> None:
        pass

    @abstractmethod
    def save_readers_to_db(self, readers_obj: list):
        pass

    @abstractmethod
    def add_book_to_db(self, books_obj: Book) -> None:
        pass

    @abstractmethod
    def delete_book_from_db(self, books_obj: Book) -> None:
        pass

    @abstractmethod
    def add_reader_to_db(self, reader_obj: Reader) -> None:
        pass

    @abstractmethod
    def delete_reader_from_db(self, reader_obj: Reader) -> None:
        pass

    @abstractmethod
    def change_book_in_db(self, books_obj: Book) -> bool:
        pass

    @abstractmethod
    def change_reader_in_db(self, reader_obj: Reader) -> bool:
        pass

    @abstractmethod
    def load_reader_by_id(self, reader_id: int) -> Reader:
        pass

    @abstractmethod
    def load_reader_by_email(self, email: str) -> Reader:
        pass

    @abstractmethod
    def select_books_by_asc(self, sort_key: int) -> list:
        pass

    @abstractmethod
    def select_books_by_desc(self, sort_key: int) -> list:
        pass

    @abstractmethod
    def select_readers_by_asc(self, sort_key: int) -> list:
        pass

    @abstractmethod
    def select_readers_by_desc(self, sort_key: int) -> list:
        pass
