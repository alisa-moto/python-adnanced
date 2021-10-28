from book import Book
from library import Library
from reader import Reader


def choose_command():
    print("Administrator commands:\nAdd book: 1\nDelete book: 2\nGive book to a reader: 3\n"
          "Get back book from the reader: 4\nList all books: 5\n"
          "List all available books: 6\nList all unavailable books: 7\nSort books by name: 8\nSort books by author: 9\n"
          "Sort books by year: 10\nDelete reader: 11\nView all readers: 12\n"
          "View readers with book: 13\n\nReader commands:\nAdd reader account: 14\nTake book from library: 15\n"
          "Give book back to library: 16\n")
    while True:
        admin_command = input("Please enter code of one of the command above: ")
        if admin_command.isdigit():
            return int(admin_command)
        else:
            print("You have entered not a valid command code.")


def execute_command(command_key):
    reader = Reader()
    if command_key == 1:
        lib.add_book_to_library()
    if command_key == 2:
        lib.delete_book_from_library()
    if command_key == 3:
        lib.give_book_to_reader(*Library.ask_for_ids())
    if command_key == 4:
        lib.take_book_from_reader(*Library.ask_for_ids())
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
        lib.delete_reader()
    if command_key == 12:
        lib.print_all_readers()
    if command_key == 13:
        lib.print_readers_with_book()
    if command_key == 14:
        lib.readers_list.append(reader.create_reader())
    if command_key == 15:
        lib.give_book_to_reader(*Reader.reader_take_or_give_book())
    if command_key == 16:
        lib.take_book_from_reader(*Reader.reader_take_or_give_book())


if __name__ == '__main__':

    books = [
        Book(1, 'Ring', 'Marek Zorica', 1994, None),
        Book(2, 'Song', 'Anton Iggy', 1984, 1),
        Book(3, 'Lullaby', 'Robert B. Wide', 2020, None),
    ]

    readers = [
        Reader(1, 'Mini', 'Driver', 2005, 2),
        Reader(2, 'Glen', 'Johnson', 1975, None),
        Reader(3, 'Nina', 'Hagen', 1887, None),
    ]

    lib = Library(books, readers)

    execute_command(choose_command())
    lib.print_all_books()
    lib.print_all_readers()
