import sys
from prime_factorization import prime_factorization
from square_root import square_root


def get_a(equation_list):
    print('returning a')
    for term in equation_list:
        if term.degree == '2':
            return term.coeff
    return None

def get_b(equation_list):
    print('returning b')
    for term in equation_list:
        if term.degree == '1':
            return term.coeff
    return None


def get_c(equation_list):
    print('returning c')
    for term in equation_list:
        if term.degree == '0':
            return term.coeff
    return None


def get_discriminant(a, b, c):
    print('returning discriminant')
    # b2 - 4ac
    d = b * b - 4 * a * c
    return d


def handle_discriminant(discriminant):
    if discriminant > 0:
        print("Discriminant is strictly positive, the two solutions are:")
        return 2
    elif discriminant == 0:
        print("Discriminant is 0, the solution is:")
        return 1
    else:
        print("Discriminant is strictly negative, there is no real solutions")
        return 0


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
    real_root = None
    real_root = -b / (2 * a)
    print('The solution is:', round(real_root, 6))


def solve_complex_roots(a, b, discriminant):
    # when D < 0
    print('solving complex things.')
    discriminant *= -1
    complex_root_1 = - b / (2 * a), ' + i', square_root(discriminant)
    complex_root_2 = - b / (2 * a), ' - i', square_root(discriminant)
    print(complex_root_1)
    print(complex_root_2)


def solve_equation(degree, equation_list):
    a = get_a(equation_list)
    b = get_b(equation_list)
    c = get_c(equation_list)
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

    #print('The solution is:')
