
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
