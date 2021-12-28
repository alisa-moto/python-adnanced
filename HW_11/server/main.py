import socket
from HW_11.server.utils.msg_utils import send_msg, recv_msg, default_encoding

N = 5

sock = socket.socket()
sock.bind(('', 1234))

sock.listen(1)

conn, client_address = sock.accept()
print(f'Accept new connection: {client_address}')

data = recv_msg(conn)
print(data.decode(default_encoding))

send_msg('Thanks'.encode(default_encoding), conn)

# data = b''
#
# while True:
#     recv_data = conn.recv(N)
#     print(f'recv_data = {recv_data.decode("866")}')
#
#     if not recv_data:
#         break
#
#     data += recv_data
#
# data = conn.recv(1024)
#
# print(data.decode('866'))
#
# conn.send(str(len(data)).encode('866')) # 99
#
# conn.close()
