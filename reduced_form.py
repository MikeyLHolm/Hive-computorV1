import sys


def reduced_form(equation_list):
    reduced_form = 'Reduced form: ' + str(equation_list[0].coeff) + ' * X^' + str(equation_list[0].degree)

    for term in equation_list[1:]:
        sign = ' + '
        if float(term.coeff) < 0:
            sign = ' - '
        reduced_form = reduced_form + sign + str(term.coeff).strip('-') + ' * X^' + str(term.degree)

    reduced_form = reduced_form + ' = 0'
    print(reduced_form)



