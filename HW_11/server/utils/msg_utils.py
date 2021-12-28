from socket import socket

default_header_size = 80
default_pack_size = 20
default_encoding = '866'

msg_1 = 'hello'
msg_2 = 'hellohellohellohellohello'


def send_msg(msg: bytes, conn: socket, header_size: int = default_header_size) -> bool:
    # estimate msg size, prepare the header
    msg_size = f'{len(msg):{header_size}}'

    # send the header
    if conn.send(msg_size.encode(default_encoding)) != header_size:
        print(f'Error: can`t send size message')
        return False

    if conn.send(msg) != len(msg):
        print(f'Error: can`t send message')
        return False

    return True


def recv_msg(conn: socket,
             header_size: int = default_header_size,
             size_pack: int = default_pack_size):
    data = conn.recv(header_size)
    if not data or len(data) != header_size:
        print('Error: can`t read size message.')
        return False

    size_msg = int(data.decode(default_encoding))
    msg = b''

    while True:
        if size_msg <= default_pack_size:
            pack = conn.recv(size_msg)
            if not pack:
                return False

            msg += pack
            break

        pack = conn.recv(size_pack)
        if not pack:
            return False

        size_msg -= size_pack
        msg += pack

    return msg



