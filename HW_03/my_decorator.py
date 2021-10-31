import time
import functools


class DecorTimeCrit:
    """Создать класс декоратор (DecorTimeCrit) класса. Декоратор, который измеряет время выполнения каждого метода,
    и печатает предупреждение, только если время выполнения было больше критического (параметр critical_time)
    p.s. подумайте на предмет функтора..."""

    def __init__(self, critical_time=0.1):
        self.critical_time = critical_time

    def __call__(self, obj_inst):
        return self.apply_to_methods(obj_inst, self.critical_time)

    @staticmethod
    def check_for_critical_time(method, critical_time):

        @functools.wraps(method)
        def time_checker(*args, **kwargs):
            method_start_time = time.monotonic()
            result = method(*args, **kwargs)
            method_end_time = time.monotonic()
            method_pass_time = method_end_time - method_start_time
            if method_pass_time > critical_time:
                print(f'WARNING! {method.__name__} is being very slow. '
                      f'It was running during {method_pass_time} seconds.')
            return result

        return time_checker

    @staticmethod
    def apply_to_methods(obj_inst, critical_time):
        @functools.wraps(obj_inst, updated=[])
        class MyNewClass:
            def __init__(self, *args, **kwargs):
                self.obj_inst = obj_inst(*args, **kwargs)

            def __getattr__(self, item):
                try:
                    temp_attribute = super().__getattribute__(item)
                except AttributeError:
                    pass
                else:
                    return temp_attribute

                temp_attribute = self.obj_inst.__getattribute__(item)

                if callable(temp_attribute):
                    return DecorTimeCrit.check_for_critical_time(temp_attribute, critical_time)
                else:
                    return temp_attribute

        return MyNewClass
