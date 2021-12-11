from client import start_client
from server import start_server

from time import time
from concurrent.futures import ProcessPoolExecutor


if __name__ == '__main__':
    start = time()

    with ProcessPoolExecutor() as ex:
        ex.submit(start_server)
        ex.submit(start_client)

    print(f'time = {time() - start} sec.')



# Создать клиент-серверное приложение.
#
# Клиент
# 1. генерирует простые числа в диапазоне от 0 до 2000000 (их всего 148933)
# 2. отправляет эти числа на сервер
#
# Сервер
# 1. принимает число от Клиента
# 2. проверяет, действительно ли это простое число
# 3. записывает число в файл
#
# Использовать можно любые технологии, которые вы знаете.
# Результат оценивается исключительно по скорости!