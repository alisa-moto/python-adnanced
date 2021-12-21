from HW_13.data_base.sql_units.sql_data_base import SQLDataBase

import os

from HW_13.library import Library


def choose_command():
    print(os.linesep)
    print("Administrator commands:\n"
          "Add book: 1\n"
          "Delete book: 2\n"
          "Give book to a reader: 3\n"
          "Get back book from the reader: 4\n"
          "List all books: 5\n"
          "List all available books: 6\n"
          "List all unavailable books: 7\n"
          "Sort books by asc order (1 - title, 2 - author, 3 - year): 8\n"
          "Sort books by desc order (1 - title, 2 - author, 3 - year): 9\n"
          "Create reader: 10\n"
          "Delete reader: 11\n"
          "View all readers: 12\n"
          "View readers with book: 13\n"
          "Sort readers by asc order (1 - name, 2 - surname, 3 - birth year): 14\n"
          "Sort readers by desc order (1 - name, 2 - surname, 3 - birth year): 15\n")

    while True:
        admin_command = input("Please enter code of one of the command above: ")
        if admin_command.isdigit():
            return int(admin_command)
        else:
            print("You have entered not a valid command code.")


def execute_command(_command_key):
    if _command_key == 1:
        print(lib.add_book_to_library(*Library.ask_for_book_params()))
    if _command_key == 2:
        print(lib.delete_book_from_library(Library.ask_for_id()))
    if _command_key == 3:
        print(lib.give_book_to_reader(*Library.ask_for_ids()))
    if _command_key == 4:
        print(lib.take_book_from_reader(*Library.ask_for_ids()))
    if _command_key == 5:
        for book in lib.print_all_books():
            print(book)
    if _command_key == 6:
        for book in lib.print_books_in_library():
            print(book)
    if _command_key == 7:
        for book in lib.print_taken_books():
            print(book)
    if _command_key == 8:
        for book in lib.sort_books_by_asc(Library.ask_for_id()):
            print(book)
    if _command_key == 9:
        for book in lib.sort_books_by_desc(Library.ask_for_id()):
            print(book)
    if _command_key == 10:
        print(lib.create_reader(*Library.ask_for_reader_params()))
    if _command_key == 11:
        print(lib.delete_reader(Library.ask_for_id()))
    if _command_key == 12:
        for reader in lib.print_all_readers():
            print(reader)
    if _command_key == 13:
        for reader in lib.print_readers_with_book():
            print(reader)
    if _command_key == 14:
        for reader in lib.sort_readers_by_asc(Library.ask_for_id()):
            print(reader)
    if _command_key == 15:
        for reader in lib.sort_readers_by_desc(Library.ask_for_id()):
            print(reader)


if __name__ == '__main__':
    # books = [
    #     Book('Ring', 'Marek Zorica', 1994),
    #     Book('Song', 'Anton Iggy', 1984),
    #     Book('Lullaby', 'Robert B. Wide', 2020),
    # ]
    #
    # readers = [
    #     Reader('Mini', 'Driver', 2005),
    #     Reader('Glen', 'Johnson', 1975),
    #     Reader('Nina', 'Hagen', 1887),
    # ]

    storage = SQLDataBase('postgres', 'pass123', 'postgres')
    lib = Library(storage)


    execute_command(choose_command())
