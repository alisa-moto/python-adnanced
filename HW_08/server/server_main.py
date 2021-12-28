from socket import socket

from HW_08.server.client_reader import ClientReader

from HW_08.server.library.library import Library
from HW_08.server.library.data_base_pack.json_db_load import JsonDBLoad
from HW_08.server.library.units.book import Book
from HW_08.server.library.units.reader import Reader


def run_server(server_ip: str, server_port: int, init_lib: Library):
    with socket() as sock:
        sock.bind((server_ip, server_port))
        sock.listen(2)

        while True:
            conn, client_info = sock.accept()
            client = ClientReader(conn, init_lib)
            client.start()


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234

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

    storage = JsonDBLoad('json_books.db', 'json_readers.db')
    lib = Library(storage, books, readers)

    run_server(ip, port, lib)
