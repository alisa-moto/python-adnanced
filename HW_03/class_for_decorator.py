from time import sleep

from HW_03.my_decorator import DecorTimeCrit


@DecorTimeCrit(critical_time=0.45)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


def execute_time_method_check():
    t = Test()
    t.method_1()
    t.method_2()


if __name__ == '__main__':
    execute_time_method_check()


# slow method start
# slow method finish
# WARNING! method_1 slow. Time = ??? sec.
# fast method start
# fast method finish
