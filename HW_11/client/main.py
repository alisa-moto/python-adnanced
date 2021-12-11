import socket
import time

from HW_11.utils.msg_utils import send_msg, recv_msg, default_encoding
import concurrent.futures as cf

# Клиент
# 1. генерирует простые числа в диапазоне от 0 до 2000000 (их всего 148933)
# 2. отправляет эти числа на сервер

# sock = socket.socket()
# sock.connect(('localhost', 1234))
#
#
# msg = "Hi! I'm a client! Just data-Just data-Just data-Just data-Just data-Just data-Just data-Just data-Just data" \
#       "-Just data-Just data-Just data."
#
# send_msg(msg.encode(default_encoding), sock)
#
# data = recv_msg(sock)
#
# print(data.decode(default_encoding))
#
# sock.close()


def inc(n):
    num = 0

    for i in range(n):
        num += 1
    return num


# def numbers_generator_thread():
#     start = time.time()
#     with cf.ThreadPoolExecutor(max_workers=60) as ex:
#         ex.map(inc, [100000 for _ in range(10)])
#     print(f'Time 60 threads = {time.time() - start}')
#
#
# def numbers_generator_process():
#     start = time.time()
#     with cf.ProcessPoolExecutor(max_workers=60) as ex:
#         ex.map(inc, [100000 for _ in range(10)])
#     print(f'Time 60 processes = {time.time() - start}')


if __name__ == '__main__':
    # numbers_generator_thread()
    # numbers_generator_process()
    # Time     60     threads = 0.28623342514038086
    # Time     60    processes = 0.8081469535827637

    start = time.time()
    for i in range(10):
        inc(200)
    print(f'Time one thread = {time.time() - start}')


