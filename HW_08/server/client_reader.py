from HW_08.server.library.library import Library
from HW_08.server.utils.msg_utils import send_msg, recv_msg, default_encoding

from socket import socket
from threading import Thread
import os

admin_commands = "Administrator commands:\n" \
                 "Add book: 1\n" \
                 "Delete book: 2\n" \
                 "Give book to a reader: 3\n" \
                 "Get back book from the reader: 4\n" \
                 "List all books: 5\n" \
                 "List all available books: 6\n" \
                 "List all unavailable books: 7\n" \
                 "Create reader: 8\n" \
                 "Delete reader: 9\n" \
                 "View all readers: 10\n" \
                 "View readers with book: 11"


class ClientReader(Thread):
    def __init__(self, conn: socket, lib: Library):
        super(ClientReader, self).__init__()

        self.conn = conn
        self.lib = lib

    def to_start_server(self) -> None:
        send_msg(admin_commands.encode(default_encoding), self.conn)

        while True:
            received_data = recv_msg(self.conn)
            if not received_data:
                print('There is no message. The client is disconnected')
                break

            received_data = received_data.decode(default_encoding)

            if not received_data.isdigit():
                print('It was not an integer')
                send_msg('You have entered not an integer. Connection is lost'.encode(default_encoding), self.conn)
                break

            received_data = int(received_data)

            # add book: 1
            if received_data == 1:
                book_name = self.input('Enter title of the book: ')
                if not book_name:
                    print('There was no title.')
                    send_msg('You didn`t enter a title. Connection is lost'.encode(default_encoding), self.conn)
                    break

                book_author = self.input('Enter author of the book: ')
                if not book_author:
                    print('There was no author.')
                    send_msg('You didn`t enter an author. Connection is lost'.encode(default_encoding), self.conn)
                    break

                book_date = self.input('Enter year of edition of the book: ', is_numeric=True)
                if not book_date:
                    print('There was no author.')
                    send_msg('You didn`t enter a year of edition. Connection '
                             'is lost'.encode(default_encoding), self.conn)
                    break

                _, client_data = self.lib.add_book_to_library(book_name, book_author, book_date)
                send_msg((client_data + os.linesep).encode(default_encoding), self.conn)

            # Delete book: 2
            # if received_data == 2:
            # Give book to a reader: 3
            # if received_data == 3:
            # Get back book from the reader: 4
            # if received_data == 4:
            # List all books: 5
            # if received_data == 5:
            # List all available books: 6
            # if received_data == 6:
            # List all unavailable books: 7
            # if received_data == 7:
            # Create reader: 8
            # if received_data == 8:
            # Delete reader: 9
            # if received_data == 9:
            # View all readers: 10
            # if received_data == 10:
            # View readers with book: 11
            # if received_data == 11:

        self.conn.close()

    def input(self, message: str, is_numeric: bool = False):
        send_msg(message.encode(default_encoding), self.conn)

        while True:
            client_answer = recv_msg(self.conn)
            if client_answer is False:
                return False

            client_answer = client_answer.decode(default_encoding)

            if is_numeric and client_answer.isnumeric():
                return int(client_answer)
            elif not is_numeric:
                return client_answer
            else:
                error_message = f'Invalid data: {client_answer}'
                send_msg(error_message.encode(default_encoding), self.conn)
