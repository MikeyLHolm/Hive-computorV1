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


def solve_perfect_equation(a, b, discriminant):
    # real roots
    # x = -b +- D / 2a
    solution_1 = None
    solution_2 = None
    solution_1 = (-b + square_root(discriminant)) / (2 * a)
    print(round(solution_1, 6))
    solution_2 = (-b - square_root(discriminant)) / (2 * a)
    print(round(solution_2, 6))


def solve_one_solution(a, b):
    # x = -b / 2a
    solution_1 = None
    solution_1 = -b / (2 * a)
    print('The solution is:', round(solution_1, 6))


def solve_complex_roots(a, b, c, discriminant):
    # when D < 0
    print('solving complex things. add prime factorializations')
    prime_factorization(a, b, discriminant)


def solve_equation(equation_list):
    print('Hello, solving it now. BRB')

    print('find type of the 3 possible')

    print('get a b c')
    a = get_a(equation_list)
    b = get_b(equation_list)
    c = get_c(equation_list)
    discriminant = get_discriminant(a, b, c)
    # print('a =', a)
    # print(type(a))
    # print('b =', b)
    # print(type(b))
    # print('c =', c)
    # print(type(c))
    print('discriminant is:', discriminant)
    # print(type(discriminant))
    solution_type = handle_discriminant(discriminant)
    if solution_type == 2:
        print('solution for type1 ( 2 solutions ):')
        solve_perfect_equation(a, b, discriminant)
    elif solution_type == 1:
        print('solution for type2 ( 1 solutions ):')
        solve_one_solution(a, b)
    elif solution_type == 0:
        print('solution for type3 ( 0 solutions ):')
        solve_complex_roots(a, b, c, discriminant)
    else:
        print('WTF HAPPENED? BUG AT SOLUTIONS')

    #print('The solution is:')
