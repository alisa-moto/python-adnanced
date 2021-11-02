from HW_04.my_iterator import MyIterator


class MyRange:

    def __init__(self, *args):
        self.__args = args
        self.start, self.step = 0, 1

        for i in self.__args:
            if type(i) is not int:
                raise TypeError(f'It is not an integer {type(i).__name__}')

        if len(self.__args) < 1:
            raise TypeError("Put at least one argument")
        elif len(self.__args) == 1:
            self.end = self.__args[0]
            self.result = self.get_numbers(self.start - self.step, self.end - self.step, self.step)
        elif len(self.__args) == 2:
            self.start = self.__args[0]
            self.end = self.__args[1]
            self.result = self.get_numbers(self.start - self.step, self.end - self.step, self.step)
        elif len(self.__args) == 3:
            self.start = self.__args[0]
            self.end = self.__args[1]
            self.step = self.__args[2]
            self.result = self.get_numbers(self.start - self.step, self.end - self.step, self.step)
        else:
            raise TypeError(f"You've provided not 3 but {len(self.__args)}")

    def __iter__(self):
        return MyIterator(self)

    @staticmethod
    def get_numbers(start, end, step):
        if step == 0:
            raise ValueError("Step cannot be equal zero.")
        if start < end and step < 0:
            raise TypeError("Step should not be lesser than zero if start point is lesser than end point.")
        if start < end:
            while start < end:
                start += step
                yield start
        else:
            while start > end and step < 0:
                start += step
                yield start
