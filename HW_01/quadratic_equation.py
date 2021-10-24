import math

'''Программа принимает от пользователя диапазоны для коэффициентов a, b, c 
квадратного уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных 
коэффициентов в указанных диапазонах, определяет квадратные уравнения, которые имеют решение'''


def enter_coefficients():
    while True:
        try:
            a1, a2, b1, b2, c1, c2 = input("Please enter coefficients range for the equation 'ax^2 + bx + c = 0' "
                                           "(6 digits). They have to be integers and be split by commas: ").split(',')
            return int(a1), int(a2), int(b1), int(b2), int(c1), int(c2)
        except ValueError:
            print("Could you check your input is as an example '1,2,1,2,1,2' and try to enter numbers again.")


def discriminant_calculation(a, b, c):
    return b ** 2 - 4 * a * c


def root_check(a1, a2, b1, b2, c1, c2):
    print(f'a1 = {a1:<3} a2 = {a2:<3} b1 = {b1:<3} b2 = {b2:<3} c1 = {c1:<3} c2 = {c2:<3}')
    for a in range(a1, a2+1):
        for b in range(b1, b2+1):
            for c in range(c1, c2+1):
                temp_discriminant = discriminant_calculation(a, b, c)
                if a == 0:
                    continue
                elif temp_discriminant > 0:
                    x1 = round((-b + math.sqrt(temp_discriminant)) / (2 * a), 2)
                    x2 = round((-b - math.sqrt(temp_discriminant)) / (2 * a), 2)
                    print(f'a = {a:<3} b = {b:<3} c = {c:<3} D = {temp_discriminant:<3} x1 = {x1:<8} x2 = {x2:<8}')
                elif temp_discriminant == 0:
                    x = -b / (2 * a)
                    print(f'a = {a:<3} b = {b:<3} c = {c:<3} D = {temp_discriminant:<3} x = {x:<8} '
                          f' it is a linear equation')
                else:
                    # print(f' There are no roots and D = {temp_discriminant}')
                    continue
    else:
        print("There is no valid example with the roots anymore")


root_check(*enter_coefficients())
