from abc import ABC, abstractmethod
"""The module for initial load from any file type to database"""


class BaseLoad(ABC):
    @abstractmethod
    def load_books_from_txt_file(self):
        pass

    @abstractmethod
    def load_readers_from_txt_file(self):
        pass
