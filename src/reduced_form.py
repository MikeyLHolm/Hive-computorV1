import sys


def reduced_form(object_list):
    for term in object_list:
        print(term)

    if not object_list:
        raise SystemExit('Reduced form: 0 = 0. All real numbers are the solution')

    reduced_form = 'Reduced form: ' + str(round(object_list[0].coeff, 6)) + ' * X^' + str(object_list[0].degree)

    for term in object_list[1:]:
        sign = ' + '
        if float(term.coeff) < 0:
            sign = ' - '
        reduced_form = reduced_form + sign + str(round(term.coeff, 6)).strip('-') + ' * X^' + str(term.degree)

    reduced_form = reduced_form + ' = 0'
    print(reduced_form)
