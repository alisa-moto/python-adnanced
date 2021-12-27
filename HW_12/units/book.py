from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from HW_12.data_base.sql_units.base_sqlalchemy import Base

"""
The module for the item "Book"
"""


class Book(Base):
    """Part for table in data base creation"""
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    book_name = Column(String, nullable=False)
    book_author = Column(String, nullable=False)
    book_date = Column(Integer, nullable=False)
    book_id_reader = Column(Integer, ForeignKey('readers.reader_id'), nullable=True)
    reader = relationship('Reader', backref='books')

    """Class to create book in library with unique parameter book_id to each item"""
    def __init__(self, book_name: str,
                 book_author: str,
                 book_date: int,
                 book_id_reader: int = None) -> None:
        self.book_name = book_name
        self.book_author = book_author
        self.book_date = book_date
        """Change book_id_reader to a reader's id if book is being taken by this reader. 
        None if book is in the library."""
        self.book_id_reader = book_id_reader

    def __str__(self):
        return f'Book id: {self.book_id}, "{self.book_name}", {self.book_author}, {self.book_date}'

    def __repr__(self):
        cls_name = __class__.__name__
        return ' '.join(
            [
                f'{attr.replace(f"_{cls_name}__", "")} = {getattr(self, attr)}'
                for attr in dir(self) if attr.startswith(f'_{cls_name}__')
            ]
        )

    def get_book_id(self) -> int:
        return self.book_id

    def get_book_name(self) -> str:
        return self.book_name

    def get_book_author(self) -> str:
        return self.book_author

    def get_book_date(self) -> int:
        return self.book_date

    def get_book_id_reader(self) -> int:
        return self.book_id_reader

    def set_book_id_reader(self, book_id_reader: int) -> None:
        self.book_id_reader = book_id_reader

    def book_to_dict(self) -> dict:
        return {
            "book_id": self.__book_id,
            "book_name": self.__book_name,
            "book_author": self.__book_author,
            "book_date": self.__book_date,
            "book_id_reader": self.__book_id_reader,
        }
    # Additional method to check all non magic attributes and revert them to dict
    # def to_dict(self) -> dict:
    #     cls_name = __class__.__name__
    #     # _Book__book_name
    #     return {
    #         attr.replace(f'_{cls_name}__', ''): getattr(self, attr)
    #         for attr in dir(self) if attr.startswith(f'_{cls_name}__')
    #     }

    @classmethod
    def book_from_dict(cls, _dict_obj: dict):
        return cls(
            book_name=_dict_obj['book_name'],
            book_author=_dict_obj['book_author'],
            book_date=_dict_obj['book_date'],
            book_id_reader=_dict_obj['book_id_reader'],
        )

    def get_all_param(self, book_obj):
        self.book_id = book_obj.book_id
        self.book_name = book_obj.book_name
        self.book_author = book_obj.book_author
        self.book_date = book_obj.book_date
        self.book_id_reader = book_obj.book_id_reader
