import sys


def reduced_form(equation_list):
    if not equation_list:
        raise SystemExit('Reduced form: 0 = 0. All the real numbers are the solution')

    reduced_form = 'Reduced form: ' + str(equation_list[0].coeff) + ' * X^' + str(equation_list[0].degree)

    for term in equation_list[1:]:
        sign = ' + '
        if float(term.coeff) < 0:
            sign = ' - '
        reduced_form = reduced_form + sign + str(term.coeff).strip('-') + ' * X^' + str(term.degree)

    reduced_form = reduced_form + ' = 0'
    print(reduced_form)
