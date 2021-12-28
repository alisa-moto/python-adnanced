from socket import socket
from HW_08.client.utils.msg_utils import send_msg, recv_msg, default_encoding


def run_client(client_ip, client_port):
    with socket() as sock:
        sock.connect((client_ip, client_port))
        # client_msg = input("Please enter your name to proceed or 'bye' to exit: ")
        #
        # while client_msg.lower().strip() != 'bye':
        while True:
            received_data = recv_msg(sock)
            if not received_data:
                print('There is no message. Try again later.')
                break

            client_msg = input(received_data.decode(default_encoding))

            send_msg(client_msg.encode(default_encoding), sock)


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1234
    run_client(ip, port)


