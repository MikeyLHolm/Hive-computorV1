import sys
from solve_utils import get_a, get_b, get_c, get_discriminant, handle_discriminant
from square_root import square_root


def solve_degree_one(b, c):
    # x = -c / b
    x = -c / b
    print('The solution is:')
    print(round(x, 6))

def solve_real_roots(a, b, discriminant):
    # x = -b +- D / 2a
    # x_1 = None
    # x_2 = None
    x_1 = (-b + square_root(discriminant)) / (2 * a)
    x_2 = (-b - square_root(discriminant)) / (2 * a)
    print(round(x_1, 6))
    print(round(x_2, 6))


def solve_real_root(a, b):
    # x = -b / 2a
    # x = None
    x = -b / (2 * a)
    print('The solution is:')
    print(round(x, 6))


def solve_complex_roots(a, b, discriminant):
    # when D < 0
    print('solving complex things.')
    discriminant *= -1
    x_1 = - b / (2 * a), ' + i', square_root(discriminant)
    x_2 = - b / (2 * a), ' - i', square_root(discriminant)
    print(round(x_1, 6))
    print(round(x_2, 6))


def solve_equation(degree, object_list):
    a = get_a(object_list)
    b = get_b(object_list)
    c = get_c(object_list)
    abc = (a, b, c)

    if degree == 1:
        solve_degree_one(b, c)
    else:
        discriminant = get_discriminant(a, b, c)
        solution_type = handle_discriminant(discriminant)

        if solution_type == 2:
            print('solution for type1 ( 2 solutions ):')
            solve_real_roots(a, b, discriminant)
        elif solution_type == 1:
            print('solution for type2 ( 1 solutions ):')
            solve_real_root(a, b)
        elif solution_type == 0:
            print('solution for type3 ( 0 solutions ):')
            solve_complex_roots(a, b, discriminant)
        else:
            print('WTF HAPPENED? BUG AT SOLUTIONS')

    return abc
