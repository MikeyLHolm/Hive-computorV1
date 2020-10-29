import sys


# add protection for 0 as coeff.
def sort_get_degree(term):
    return (term.degree)


def handle_degree(equation_list):
    degree = -1

    for obj in equation_list:
        try:
            if int(obj.degree) > degree:
                degree = int(obj.degree)
        except ValueError:
            raise SystemExit('Degree must be an Integer!')

    print("Polynomial degree:", degree)
    if degree > 2:
        raise SystemExit('The polynomial degree is stricly greater than 2, I can\'t solve.')
    if degree < 1:
        raise SystemExit('The polynomial degree is smaller than 1, I can\'t solve. Bad input!')
    return degree
