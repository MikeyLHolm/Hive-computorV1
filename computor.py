#!/usr/bin/env python3

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 - 3 * X^2"
# 1 * X^2 + 2 * X^1 - 3 * X^0 = 0
# python3 computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# python3 computor.py "2 * X^0 + 4 * X^1 + 2 * X^2 = 0" ==> -1.0
# 2 * X^0 + 4 * X^1 + 2 * X^2 = 0

# FROM SUBJECT:
# python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"
# 42 * X^0 = 42 * X^0


# TO DO:
# add protection for float degrees
# XX^2 etc?
# fix 0 as coeff
#

import sys
from degree import handle_degree, sort_get_degree
from handle_complex_input import handle_complex_input
from int_or_float import handle_int_or_float
from object_related import get_list_of_objects, clean_object_list
from plotting import plot
from read_and_parse import handle_zero_degree_form, parse_input, read_input, remove_empty_items
from reduced_form import reduced_form
from solve_equation import solve_equation


def main():
    data, to_plot = read_input()
    print(data)
    left_list, right_list = parse_input(data)
    left_list, right_list = handle_complex_input(left_list, right_list)
    print(left_list)
    print(right_list)

    object_list = []
    object_list = get_list_of_objects(left_list, right_list)
    object_list.sort(key=sort_get_degree, reverse=True)

    handle_int_or_float(object_list)

    cleaned_object_list = []
    cleaned_object_list = clean_object_list(object_list)

    reduced_form(cleaned_object_list)
    degree = handle_degree(cleaned_object_list)

    abc = ()
    abc = solve_equation(degree, cleaned_object_list)
    if to_plot == 'Y':
        plot(abc)


if __name__ == "__main__":
    main()
