class MyIterator:
    """Class to create iterable object
    It takes object with main logic for range creation"""
    def __init__(self, my_range_obj):
        self.my_range_obj = my_range_obj

    def __next__(self):
        """Overrided __next__ method to obtain some object and go through all of the elements till the end of
        a created range"""
        self.get_iterator = self.my_range_obj.result
        for i in self.get_iterator:
            return i
        raise StopIteration
