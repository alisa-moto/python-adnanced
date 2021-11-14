from .utils.book import Book
from .library import Library
from .utils.reader import Reader


def choose_command():
    print("Administrator commands:\nAdd book: 1\nDelete book: 2\nGive book to a reader: 3\n"
          "Get back book from the reader: 4\nList all books: 5\n"
          "List all available books: 6\nList all unavailable books: 7\nSort books by name: 8\nSort books by author: 9\n"
          "Sort books by year: 10\nCreate reader: 11\nDelete reader: 12\nView all readers: 13\n"
          "View readers with book: 14\nSort readers by first name: 15\nSort readers by last name: 16\n"
          "Sort readers by birth year: 17\n")
    while True:
        admin_command = input("Please enter code of one of the command above: ")
        if admin_command.isdigit():
            return int(admin_command)
        else:
            print("You have entered not a valid command code.")


def execute_command(command_key):
    if command_key == 1:
        print(lib.add_book_to_library(*Library.ask_for_book_params()))
    if command_key == 2:
        print(lib.delete_book_from_library())
    if command_key == 3:
        print(lib.give_book_to_reader(*Library.ask_for_ids()))
    if command_key == 4:
        print(lib.take_book_from_reader(*Library.ask_for_ids()))
    if command_key == 5:
        lib.print_all_books()
    if command_key == 6:
        lib.print_books_in_library()
    if command_key == 7:
        lib.print_taken_books()
    if command_key == 8:
        lib.sort_books_by_name()
    if command_key == 9:
        lib.sort_books_by_author()
    if command_key == 10:
        lib.sort_books_by_date()
    if command_key == 11:
        print(lib.create_reader(*Library.ask_for_reader_params()))
    if command_key == 12:
        print(lib.delete_reader())
    if command_key == 13:
        lib.print_all_readers()
    if command_key == 14:
        lib.print_readers_with_book()
    if command_key == 15:
        lib.sort_reader_by_first_name()
    if command_key == 16:
        lib.sort_reader_by_last_name()
    if command_key == 17:
        lib.sort_reader_by_birth_year()


if __name__ == '__main__':

    books = [
        Book('Ring', 'Marek Zorica', 1994),
        Book('Song', 'Anton Iggy', 1984),
        Book('Lullaby', 'Robert B. Wide', 2020),
    ]

    readers = [
        Reader('Mini', 'Driver', 2005),
        Reader('Glen', 'Johnson', 1975),
        Reader('Nina', 'Hagen', 1887),
    ]

    lib = Library(books, readers)

    lib.print_all_books()
    lib.print_all_readers()
    execute_command(choose_command())
    lib.print_all_books()
    lib.print_all_readers()
