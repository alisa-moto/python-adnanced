from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from HW_site.library.data_base.sql_units.base_sqlalchemy import Base

"""
The module for the item "Reader"
"""


class Reader(Base):
    """Part for table in data base creation"""
    __tablename__ = 'readers'

    reader_id = Column(Integer, primary_key=True, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
    book_id_reader = Column(Integer, nullable=True)

    """Class to create reader in library with unique parameter reader_id to each item"""
    def __init__(self, first_name: str,
                 last_name: str,
                 birth_year: int,
                 reader_book_id: int = None) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        """Change reader_book_id to a book's id if reader took this book. 
        None if reader does not have any book."""
        self.reader_book_id = reader_book_id

    def __str__(self):
        return f'Reader id: {self.reader_id}, {self.first_name}, {self.last_name}, {self.birth_year}'

    def __repr__(self):
        cls_name = __class__.__name__
        return ' '.join(
            [
                f'{attr.replace(f"_{cls_name}__", "")} = {getattr(self, attr)}'
                for attr in dir(self) if attr.startswith(f'_{cls_name}__')
            ]
        )

    def get_reader_id(self) -> int:
        return self.reader_id

    def get_reader_first_name(self) -> str:
        return self.first_name

    def get_reader_last_name(self) -> str:
        return self.last_name

    def get_birth_year(self) -> int:
        return self.birth_year

    def get_reader_book_id(self) -> int:
        return self.reader_book_id

    def set_reader_book_id(self, reader_book_id: int) -> None:
        self.reader_book_id = reader_book_id

    def reader_to_dict(self) -> dict:
        return {
            "reader_id": self.reader_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_year": self.birth_year,
            "reader_book_id": self.reader_book_id,
        }

    @classmethod
    def reader_from_dict(cls, dict_obj: dict):
        return cls(
            reader_id=dict_obj['reader_id'],
            first_name=dict_obj['first_name'],
            last_name=dict_obj['last_name'],
            birth_year=dict_obj['birth_year'],
            reader_book_id=dict_obj['reader_book_id'],
        )

    def get_all_param(self, reader_obj):
        self.reader_id = reader_obj.reader_id
        self.first_name = reader_obj.first_name
        self.last_name = reader_obj.last_name
        self.birth_year = reader_obj.birth_year
        self.reader_book_id = reader_obj.reader_book_id
