from book import Book
from library import Library
from reader import Reader

# Add reader:

def choose_user():
    users = {1: enter_admin_command(), 2: enter_reader_command()}
    while True:
        user_type = input("Please enter '1' for admin or '2' for reader: ")
        if user_type.isdigit():
            return users.get(int(user_type))
        else:
            print("You have entered not a valid command code.")


def enter_admin_command():
    print("Add book: 1\nDelete book: 2\nGive book to a reader: 3\nGet back book from the reader: 4\nList all books: 5\n"
          "List all available books: 6\nList all unavailable books: 7\nSort books by name: 8\nSort books by author: 9\n"
          "Sort books by year: 10\nDelete reader: 11\nView all readers: 12\n"
          "View readers with book: 13\n")
    while True:
        admin_command = input("Please enter code of one of the command above: ")
        if admin_command.isdigit():
            return int(admin_command)
        else:
            print("You have entered not a valid command code.")

def enter_reader_command():
    print("Add reader account: 14\nTake book from library: 15\nGive book back to library: 16")
    while True:
        reader_command = input("Please enter code of one of the command above: ")
        if reader_command.isdigit():
            return int(reader_command)
        else:
            print("You have entered not a valid command code.")


if __name__ == '__main__':

    books = [
        Book(1, 'Book1', 'Anton Zorich', 1994, None),
        Book(2, 'Book2', 'Marek Igny', 1984, 1)
    ]

    readers = [
        Reader(1, 'Mini', 'Driver', 2005, None),
        Reader(2, 'Glen', 'Johnson', 1975, None)
    ]


    # lib = Library(books, [])
    # lib.add_book_to_library(3, 'Book3', 'John Silver', 2004)
    # lib.print_all_books()
    # lib.print_books_in_library()
    # lib.print_taken_books()
    # lib.delete_book_from_library()
    # lib.print_all_books()
    # lib.sort_books_by_name()
    # lib.sort_books_by_author()
    # lib.sort_books_by_date()
    # lib.give_book_to_reader(*Library.ask_for_ids())
    # lib.print_all_books()
    # lib.print_all_readers()
    # lib.take_book_from_reader(1, 2)
    # lib.print_all_books()
    # lib.print_all_readers()
    # lib.create_reader()
    # lib.print_all_readers()
    # lib.add_book_to_library()
    # lib.print_all_books()
    # reader = Reader()
    # lib.readers_list.append(reader.create_reader())
    # lib.print_all_readers()


    def choose_command(command_key):
        lib = Library(books, readers)
        reader = Reader()
        commands = {1: lib.add_book_to_library(),
                    2: lib.give_book_to_reader(*Library.ask_for_ids()),
                    3: lib.give_book_to_reader(*Library.ask_for_ids()),
                    4: lib.take_book_from_reader(*Library.ask_for_ids()),
                    5: lib.print_all_books(),
                    6: lib.print_books_in_library(),
                    7: lib.print_taken_books(),
                    8: lib.sort_books_by_name(),
                    9: lib.sort_books_by_author(),
                    10: lib.sort_books_by_date(),
                    11: lib.readers_list.append(reader.create_reader()),
                    12: lib.delete_reader(),
                    13:
                    14:
                    15: }
        return commands.get(command_key)

    choose_command(1)




