import sys
from solve_utils import get_a, get_b, get_c, get_discriminant, handle_discriminant
from square_root import square_root


def solve_real_roots(a, b, discriminant):
    # x = -b +- D / 2a
    # real_root_1 = None
    # real_root_2 = None
    real_root_1 = (-b + square_root(discriminant)) / (2 * a)
    real_root_2 = (-b - square_root(discriminant)) / (2 * a)
    print(round(real_root_1, 6))
    print(round(real_root_2, 6))


def solve_real_root(a, b):
    # x = -b / 2a
    # real_root = None
    real_root = -b / (2 * a)
    print('The solution is:', round(real_root, 6))


def solve_complex_roots(a, b, discriminant):
    # when D < 0
    print('solving complex things.')
    discriminant *= -1
    complex_root_1 = - b / (2 * a), ' + i', square_root(discriminant)
    complex_root_2 = - b / (2 * a), ' - i', square_root(discriminant)
    print(round(complex_root_1, 6))
    print(round(complex_root_2, 6))


def solve_equation(degree, equation_list):
    a = get_a(equation_list)
    b = get_b(equation_list)
    c = get_c(equation_list)
    abc = (a, b, c)
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
