import os
import socket

admin_commands = "Administrator commands:\n" \
                 "Add book: 1\n" \
                 "Delete book: 2\n" \
                 "Give book to a reader: 3\n" \
                 "Get back book from the reader: 4\n" \
                 "List all books: 5\n" \
                 "List all available books: 6\n" \
                 "List all unavailable books: 7\n" \
                 "Sort books by name: 8\n" \
                 "Sort books by author: 9\n" \
                 "Sort books by year: 10\n" \
                 "Create reader: 11\n" \
                 "Delete reader: 12\n" \
                 "View all readers: 13\n" \
                 "View readers with book: 14\n" \
                 "Sort readers by first name: 15\n" \
                 "Sort readers by last name: 16\n" \
                 "Sort readers by birth year: 17\n"



# def execute_command(_command_key):
#     if _command_key == 1:
#         print(lib.add_book_to_library(*Library.ask_for_book_params()))
#     if _command_key == 2:
#         print(lib.delete_book_from_library())
#     if _command_key == 3:
#         print(lib.give_book_to_reader(*Library.ask_for_ids()))
#     if _command_key == 4:
#         print(lib.take_book_from_reader(*Library.ask_for_ids()))
#     if _command_key == 5:
#         lib.print_all_books()
#     if _command_key == 6:
#         lib.print_books_in_library()
#     if _command_key == 7:
#         lib.print_taken_books()
#     if _command_key == 8:
#         lib.sort_books_by_name()
#     if _command_key == 9:
#         lib.sort_books_by_author()
#     if _command_key == 10:
#         lib.sort_books_by_date()
#     if _command_key == 11:
#         print(lib.create_reader(*Library.ask_for_reader_params()))
#     if _command_key == 12:
#         print(lib.delete_reader())
#     if _command_key == 13:
#         lib.print_all_readers()
#     if _command_key == 14:
#         lib.print_readers_with_book()
#     if _command_key == 15:
#         lib.sort_reader_by_first_name()
#     if _command_key == 16:
#         lib.sort_reader_by_last_name()
#     if _command_key == 17:
#         lib.sort_reader_by_birth_year()

def choose_command(user_name):
    while True:
        admin_command = input(f'Hi {user_name}! Please enter code of one of the command above: ')
        if admin_command.isdigit():
            return int(admin_command)
        else:
            return "You have entered not a valid command code."


def server():
    sock = socket.socket()
    sock.bind(('', 1234))

    sock.listen(1)

    conn, client_address = sock.accept()
    print(f'Accept new connection: {client_address}')

    # conn.send(admin_commands.encode())

    while True:
        received_data = conn.recv(1024).decode()
        if not received_data:
            break
        print(f'Received from client: {received_data}')
        conn.send(admin_commands.encode())
        while True:
            admin_command = input(f'Hi {received_data}! Please enter code of one of the command above: ')
            conn.send(admin_command.encode())
            if admin_command.isdigit():
                return int(admin_command)
            else:
                return "You have entered not a valid command code."


if __name__ == '__main__':
    server()
