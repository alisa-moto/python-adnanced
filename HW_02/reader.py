class Reader:
    def __init__(self, reader_id=1, first_name='John', last_name='Meany', birth_year=1990, reader_book_id=None):
        self.reader_id = reader_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.reader_book_id = reader_book_id

    @staticmethod
    def reader_take_or_give_book():
        while True:
            reader_book_id, reader_id = input("Please enter book id and your library card id split by comma: "
                                              "").split(',')
            if reader_book_id.isdigit() and reader_id.isdigit():
                return int(reader_book_id), int(reader_id)
            else:
                print("You have entered not a valid positive integers as ids.")

    @staticmethod
    def create_reader():
        reader_id, first_name, last_name, birth_year = input("Please enter your id, first name, last name, birth "
                                                             "year split by comma as in the example '4,Linn,Lindon,"
                                                             "1997': ").split(',')
        return Reader(reader_id, first_name, last_name, birth_year, None)
