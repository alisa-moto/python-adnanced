from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from HW_13.data_base.base_db import BaseDB
from HW_13.data_base.sql_units.base_sqlalchemy import Base
from HW_13.units.book import Book
from HW_13.units.reader import Reader


class SQLDataBase(BaseDB):
    def __init__(self, data_base_user: str,
                 data_base_password: str,
                 data_base_name: str,
                 data_base_address: str = 'localhost',
                 data_base_port: int = 5432,
                 dialect: str = 'postgresql'):

        self.__engine = create_engine(f'{dialect}://{data_base_user}:{data_base_password}@{data_base_address}:'
                                      f'{data_base_port}/{data_base_name}')

        # create table
        Base.metadata.create_all(self.__engine)
        # start session
        self.__session = Session(self.__engine)

    def load_books_from_db(self) -> list:
        return self.__session.query(Book).all()

    def load_books_from_db_by_input(self, **kwargs):
        for key, _ in kwargs.items():
            if key not in dir(Book):
                return None

        return self.__session.query(Book).filter_by(**kwargs).all()

    def add_book_to_db(self, books_obj: Book) -> bool:
        self.__session.add(books_obj)
        try:
            self.__session.commit()
        except:
            return False
        return True

    def save_books_to_db(self, books_obj: list):
        self.__session.add_all(books_obj)
        try:
            self.__session.commit()
        except:
            return False
        return True

    def delete_book_from_db(self, books_obj: Book) -> bool:
        self.__session.delete(books_obj)
        try:
            self.__session.commit()
        except:
            return False
        return True

    def change_book_in_db(self, books_obj: Book) -> bool:
        book = self.__session.query(Book).filter(Book.book_id == books_obj.book_id).first()

        if not book:
            return False

        book.get_all_param(books_obj)

        try:
            self.__session.commit()
        except:
            return False
        return True

    def load_readers_from_db(self) -> list:
        return self.__session.query(Reader).all()

    def load_reader_from_db_by_input(self, **kwargs):
        for key, _ in kwargs.items():
            if key not in dir(Reader):
                return None

        return self.__session.query(Reader).filter_by(**kwargs)

    def add_reader_to_db(self, reader_obj: Reader) -> bool:
        self.__session.add(reader_obj)
        try:
            self.__session.commit()
        except:
            return False
        return True

    def save_readers_to_db(self, readers_obj: list):
        self.__session.add_all(readers_obj)
        try:
            self.__session.commit()
        except:
            return False
        return True

    def delete_reader_from_db(self, reader_obj: Reader) -> bool:
        self.__session.delete(reader_obj)
        try:
            self.__session.commit()
        except:
            return False
        return True

    def change_reader_in_db(self, reader_obj: Reader) -> bool:
        reader = self.__session.query(Reader).filter(Reader.reader_id == reader_obj.reader_id).first()

        if not reader:
            return False

        reader.get_all_param(reader_obj)

        try:
            self.__session.commit()
        except:
            return False
        return True

    def load_reader_by_id(self, reader_id: int) -> Reader:
        return self.__session.query(Reader).filter_by(reader_id=reader_id).first()

    def load_reader_by_email(self, email: str) -> Reader:
        return self.__session.query(Reader).filter_by(email=email).first()
