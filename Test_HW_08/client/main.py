import socket


def client():
    sock = socket.socket()
    sock.connect(('localhost', 1234))

    message = input("Please enter your name or 'bye' to exit: ")

    while message.lower().strip() != 'bye':
        sock.send(message.encode())
        data = sock.recv(1024).decode()

        print(f'Received from server: {data}')

        message = input('-> ')

    sock.close()


if __name__ == '__main__':
    client()
