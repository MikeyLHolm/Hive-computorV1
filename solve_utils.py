
def get_a(object_list):
    for term in object_list:
        if term.degree == '2':
            return term.coeff
    return 0

def get_b(object_list):
    for term in object_list:
        if term.degree == '1':
            return term.coeff
    return 0


def get_c(object_list):
    for term in object_list:
        if term.degree == '0':
            return term.coeff
    return 0


def get_discriminant(a, b, c):
    # b2 - 4ac
    d = b * b - 4 * a * c
    return d


def handle_discriminant(discriminant):
    if discriminant > 0:
        print('Discriminant is strictly positive, the two solutions are:')
        return 2
    elif discriminant == 0:
        print('Discriminant is 0, the solution is:')
        return 1
    else:
        print('Discriminant is strictly negative, there is no real solutions.'
              ' The two comples roots are:')
        return 0
