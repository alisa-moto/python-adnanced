from book import Book
# from reader import Reader


class Library:
    def __init__(self, books_list, readers_list):
        self.books_list = books_list
        self.readers_list = readers_list
        # self.__present_books = self.books_list
        # self.__present_readers = self.readers_list

    def add_book_to_library(self):
        book_id, book_name, book_author, book_date = input("Please enter book id, title, author name, year of edition "
                                                           "split by comma as in the example '4,River,Enthony Bach,"
                                                           "1956': ").split(',')
        book = Book(book_id, book_name, book_author, book_date, None)
        return self.books_list.append(book)

    def delete_book_from_library(self):
        book_id = input("Please enter book id: ")
        for book in self.books_list:
            if book.book_id == int(book_id):
                self.books_list.remove(book)

    @staticmethod
    def ask_for_ids():
        while True:
            book_id, reader_id = input("Please enter book id and reader id split by comma: ").split(',')
            if book_id.isdigit() and reader_id.isdigit():
                return int(book_id), int(reader_id)
            else:
                print("You have entered not a valid positive integers as ids.")

    def give_book_to_reader(self, book_id, reader_id):
        for book in self.books_list:
            if book.book_id == book_id:
                book.book_id_reader = reader_id
        for reader in self.readers_list:
            if reader.reader_id == reader_id:
                reader.reader_book_id = book_id

    def take_book_from_reader(self, book_id, reader_id): # __present_books __present_readers
        for book in self.books_list:
            if book.book_id == book_id:
                book.book_id_reader = None
        for reader in self.readers_list:
            if reader.reader_id == reader_id:
                reader.reader_book_id = None

    def print_all_books(self):
        for book in self.books_list:
            print(book.book_id, book.book_name, book.book_author, book.book_date, book.book_id_reader)

    def print_books_in_library(self): # __present_books
        for book in self.books_list:
            if book.book_id_reader is None:
                print(book.book_id, book.book_name, book.book_author, book.book_date, book.book_id_reader)

    def print_taken_books(self): # __present_books
        for book in self.books_list:
            if book.book_id_reader is not None:
                print(book.book_id, book.book_name, book.book_author, book.book_date, book.book_id_reader)

    def sort_books_by_name(self):
        for book in sorted(self.books_list, key=lambda x: x.book_name):
            print(book.book_id, book.book_name, book.book_author, book.book_date, book.book_id_reader)

    def sort_books_by_author(self):
        for book in sorted(self.books_list, key=lambda x: x.book_author):
            print(book.book_id, book.book_name, book.book_author, book.book_date, book.book_id_reader)

    def sort_books_by_date(self):
        for book in sorted(self.books_list, key=lambda x: x.book_date):
            print(book.book_id, book.book_name, book.book_author, book.book_date, book.book_id_reader)

    def delete_reader(self):
        reader_id = input("Please enter reader id: ")
        for reader in self.readers_list:
            if reader.reader_id == int(reader_id):
                self.readers_list.remove(reader)

    def print_all_readers(self):
        for reader in self.readers_list:
            print(reader.reader_id, reader.first_name, reader.last_name, reader.birth_year, reader.reader_book_id)

    def print_readers_with_book(self): # __present_books
        for reader in self.readers_list:
            if reader.reader_book_id is not None:
                print(reader.reader_id, reader.first_name, reader.last_name, reader.birth_year, reader.reader_book_id)
