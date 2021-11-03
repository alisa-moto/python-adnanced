from HW_04.my_iterator import MyIterator


class MyRange:
    """Class for the main logic of range creation from 1, 2 or 3 integer arguments (positive or negative as well)."""
    def __init__(self, *args):
        self.__args = args
        self.start, self.step = 0, 1
        """Check to be sure we have only integers."""
        for i in self.__args:
            if type(i) is not int:
                raise TypeError(f'It is not an integer {type(i).__name__}')
        """Check if there is at least one argument provided.
        Switch to 1, 2 or 3 arguments logic if they are provided.
        1 argument: end point, as a result we have default start - default step, custom end - default step, 
        default step
        2 arguments: first var. as start point and second var. as end point, as a result we have custom start - 
        default step, custom end - default step, default step
        3 arguments: first var. as start point, second var. as end point, third var. as a step, as a result we have 
        custom start - custom step, custom end - custom step, custom step
        """
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
        """Overrided __iter__ method to get iterable objects from the custom iterator class"""
        return MyIterator(self)

    @staticmethod
    def get_numbers(start, end, step):
        """Method to generate range from custom or default step, start and end points.
        start: int, default = 0
        end: int, no default value
        step: int, default = 1, cannot be 0"""
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
