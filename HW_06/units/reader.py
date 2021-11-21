"""
The module for the item "Reader"
"""


class Reader:
    """Class to create reader in library with unique parameter reader_id to each item"""
    def __init__(self, first_name: str = 'John', last_name: str = 'Meany', birth_year: int = 1990,
                 reader_book_id: int = None, _reader_id: int = None):
        self.__reader_id = _reader_id if _reader_id is not None else int(id(self))
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_year = birth_year
        """Change reader_book_id to a book's id if reader took this book. 
        None if reader does not have any book."""
        self.__reader_book_id = reader_book_id

    def __str__(self):
        return f'Reader id: {self.__reader_id}: {self.__first_name}, {self.__last_name}, {self.__birth_year}, ' \
               f'Book id: {self.__reader_book_id}'

    def __repr__(self):
        cls_name = __class__.__name__
        return ' '.join(
            [
                f'{attr.replace(f"_{cls_name}__", "")} = {getattr(self, attr)}'
                for attr in dir(self) if attr.startswith(f'_{cls_name}__')
            ]
        )

    def get_reader_id(self) -> int:
        return self.__reader_id

    def get_reader_first_name(self) -> str:
        return self.__first_name

    def get_reader_last_name(self) -> str:
        return self.__last_name

    def get_birth_year(self) -> int:
        return self.__birth_year

    def get_reader_book_id(self) -> int:
        return self.__reader_book_id

    def set_reader_book_id(self, reader_book_id: int) -> None:
        self.__reader_book_id = reader_book_id

    def reader_to_dict(self) -> dict:
        return {
            "reader_id": self.__reader_id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "birth_year": self.__birth_year,
            "reader_book_id": self.__reader_book_id,
        }

    @classmethod
    def reader_from_dict(cls, dict_obj: dict):
        return cls(
            _reader_id=dict_obj['reader_id'],
            first_name=dict_obj['first_name'],
            last_name=dict_obj['last_name'],
            birth_year=dict_obj['birth_year'],
            reader_book_id=dict_obj['reader_book_id'],
        )
