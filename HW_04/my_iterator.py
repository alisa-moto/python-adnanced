class MyIterator:
    def __init__(self, my_range_obj):
        self.my_range_obj = my_range_obj

    def __next__(self):
        self.get_iterator = self.my_range_obj.result
        for i in self.get_iterator:
            return i
        raise StopIteration
