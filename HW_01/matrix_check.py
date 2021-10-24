import numpy as np
"""Дана матрица целых чисел 10x10. Вводится число. Выяснить, какие строки и столбцы матрицы содержат данное число.
(либо рандом либо чтение из файла (input.txt))"""

start_matrix_value = 10
end_matrix_value = 30
matrix_side = 10
nl = '\n'


def enter_checked_value():
    while True:
        int_to_check = input("Please enter positive integer for check: ")
        if int_to_check.isdigit():
            return int(int_to_check)
        else:
            print("You have entered not a valid positive integer.")


def create_random_matrix(start, end, side):
    return np.random.randint(start, end, (side, side))


def check_value_position(check_value):
    matrix = create_random_matrix(start_matrix_value, end_matrix_value, matrix_side)
    check_list_row = []
    check_list_column = []

    for row in range(matrix_side):
        for column in range(matrix_side):
            if matrix[row][column] == check_value:
                check_list_row.append(row)
                check_list_column.append(column)
    print(f' {str(matrix)[1:-1]}{nl}Numbers range: ({start_matrix_value}, {end_matrix_value}){nl}Chosen number: '
          f'{check_value}{nl}Rows: {str(check_list_row)[1:-1]}{nl}Columns: {str(check_list_column)[1:-1]}')


check_value_position(enter_checked_value())
