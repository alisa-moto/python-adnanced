from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import Session
import gevent

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

    def add_book_to_db(self, books_obj: Book) -> None:
        self.__session.add(books_obj)
        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()

    def save_books_to_db(self, books_obj: list) -> None:
        self.__session.add_all(books_obj)
        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()

    def delete_book_from_db(self, books_obj: Book) -> None:
        self.__session.delete(books_obj)
        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()

    def change_book_in_db(self, books_obj: Book) -> bool:
        book = self.__session.query(Book).filter(Book.book_id == books_obj.book_id).first()

        if not book:
            return False

        book.get_all_param(books_obj)

        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()
            return False
        return True

    def load_readers_from_db(self) -> list:
        return self.__session.query(Reader).all()

    def load_reader_from_db_by_input(self, **kwargs):
        for key, _ in kwargs.items():
            if key not in dir(Reader):
                return None

        return self.__session.query(Reader).filter_by(**kwargs)

    def add_reader_to_db(self, reader_obj: Reader) -> None:
        self.__session.add(reader_obj)
        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()

    def save_readers_to_db(self, readers_obj: list) -> None:
        self.__session.add_all(readers_obj)
        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()

    def delete_reader_from_db(self, reader_obj: Reader) -> None:
        self.__session.delete(reader_obj)
        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()

    def change_reader_in_db(self, reader_obj: Reader) -> bool:
        reader = self.__session.query(Reader).filter(Reader.reader_id == reader_obj.reader_id).first()

        if not reader:
            return False

        reader.get_all_param(reader_obj)

        try:
            self.__session.commit()
        except gevent.Timeout:
            self.__session.invalidate()
        except:
            self.__session.rollback()
            return False
        return True

    def load_reader_by_id(self, reader_id: int) -> Reader:
        return self.__session.query(Reader).filter_by(reader_id=reader_id).first()

    def load_reader_by_email(self, email: str) -> Reader:
        return self.__session.query(Reader).filter_by(email=email).first()

    def select_books_by_asc(self, sort_key: int) -> list:
        if sort_key == 1:
            return self.__session.query(Book).order_by(asc(Book.book_name))
        if sort_key == 2:
            return self.__session.query(Book).order_by(asc(Book.book_author))
        if sort_key == 3:
            return self.__session.query(Book).order_by(asc(Book.book_date))

    def select_books_by_desc(self, sort_key: int) -> list:
        if sort_key == 1:
            return self.__session.query(Book).order_by(desc(Book.book_name))
        if sort_key == 2:
            return self.__session.query(Book).order_by(desc(Book.book_author))
        if sort_key == 3:
            return self.__session.query(Book).order_by(desc(Book.book_date))

    def select_readers_by_asc(self, sort_key: int) -> list:
        if sort_key == 1:
            return self.__session.query(Reader).order_by(asc(Reader.first_name))
        if sort_key == 2:
            return self.__session.query(Reader).order_by(asc(Reader.last_name))
        if sort_key == 3:
            return self.__session.query(Reader).order_by(asc(Reader.birth_year))

    def select_readers_by_desc(self, sort_key: int) -> list:
        if sort_key == 1:
            return self.__session.query(Reader).order_by(desc(Reader.first_name))
        if sort_key == 2:
            return self.__session.query(Reader).order_by(desc(Reader.last_name))
        if sort_key == 3:
            return self.__session.query(Reader).order_by(desc(Reader.birth_year))
