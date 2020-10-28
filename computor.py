#!/usr/bin/env python3

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 - 3 * X^2"
# 1 * X^2 + 2 * X^1 - 3 * X^0 = 0
# python3 computor.py "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"
# python3 computor.py "2 * X^0 + 4 * X^1 + 2 * X^2 = 0" ==> -1.0

# FROM SUBJECT:
# python3 computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

# python3 computor.py "5 * X^0 + 4 * X^1 = 4 * X^0"


from reduced_form import reduced_form
from linked_list import Node, SLinkedList, parse_to_linked_list
from solve_equation import solve_equation
from term_object import get_list_of_objects
# from square_root import square_root
import sys

constants = []
x_1 = []
x_2 = []


def read_input():
    arg = sys.argv[1] if len(sys.argv) > 1 else "somevalue"
    return arg
    # equation = input("Enter the equation: ")
    # return equation


def parse_input(data):
    data = data.replace(" ", "").replace("^", "").replace("-", "+-")
    data = data.split("=")
    #return 2 values thru left and right side
    #return left_side(data[0]), right_side(data[1])
    return data[0].split("+"), data[1].split("+")


def save_terms_left(left):
    print("L terms are: ", left)

    for term in left:
        if term.find("X") != -1:
            print(term)
            for i, c in enumerate(term):
                if c == "X":
                    print(c)
                    print(term[i + 1])
                    if term[i + 1] == "0":
                        constants.append(term[0:i - 1])
                    elif term[i + 1] == "1":
                        x_1.append(term[0:i - 1])
                    elif term[i + 1] == "2":
                        x_2.append(term[0:i - 1])
                    else:
                        sys.exit("Other degrees not supported, EXIT")
        else:
            sys.exit("No X in a term, EXIT")


def opposite_sign(term):
    if term[0] == "-":
        return term[1:]
    else:
        return ("-" + term)


def save_terms_right(right):
    print("R terms are: ", right)

    for term in right:
        if term.find("X") != -1:
            for i, c in enumerate(term):
                if c == "X":
                    if term[i + 1] == "0":
                        constants.append(opposite_sign(term[0:i - 1]))
                    elif term[i + 1] == "1":
                        x_1.append(opposite_sign(term[0:i - 1]))
                    elif term[i + 1] == "2":
                        x_2.append(opposite_sign(term[0:i - 1]))
                    else:
                        sys.exit("Other degrees not supported, EXIT")
        else:
            sys.exit("No X in a term, EXIT")


def remove_empty_items(list_name):
    cleaned_list = [x for x in list_name if x]
    return cleaned_list


def calc_constants():
    constant = 0
    for x in constants:
        constant += int(x)
    return constant


def calc_first_degree():
    first_degree = 0
    for x in x_1:
        first_degree += int(x)
    return first_degree


def calc_second_degree():
    second_degree = 0
    for x in x_2:
        second_degree += float(x)
    return second_degree


def return_degree(side):
    degree = -1
    temp_degree = ""
    side_len = len(side)
    if side.find("X") != -1:
        for i, c in enumerate(side):
            if c == "X":
                j = i
                while (j + 1) < side_len and side[j + 1].isdigit():
                    temp_degree = temp_degree + side[j + 1]
                    j += 1
                if int(temp_degree) > degree:
                    degree = int(temp_degree)
                temp_degree = ""
    else:
        return 0
    return(degree)


def get_degree(data):
    degree_l = return_degree(data[0])
    degree_r = return_degree(data[1])
    if degree_l >= degree_r:
        return degree_l
    else:
        return degree_r


  # add protection for 0 as coeff.
def sort_get_degree(term):
    return (term.degree)


# Change mantissa to better name as this truly isn't mantissa afaik!
def str_to_float_or_int(value_str, ShowExtended=False):
    isfloat = True
    value = float(value_str)
    numberParsed = value_str.split(".")
    if len(numberParsed) > 1:
        integer = numberParsed[0]
        mantissa = numberParsed[1]
        if integer.strip('-').isdecimal() and mantissa.isdecimal():
            if int(mantissa) == 0:
                isfloat = False
                value = int(integer)
        elif integer.strip('-').isdecimal():
            isfloat = False
            value = int(integer)
    else:
        isfloat = False
        value = int(value_str)
    if ShowExtended:
        print("testValue: " + value_str + " | splits into: ",
                numberParsed,"\n value: ", value)
        if isfloat:
            print("It's a <float> (;o)\n")
        else:
            print("It's an <int> {:o)~\n")

    return value


def handle_int_or_float(equation_list):
    for term in equation_list:
        term.coeff = str_to_float_or_int(str(term.coeff))


def handle_degree(equation_list):
    degree = -1

    for obj in equation_list:
        if int(obj.degree) > degree:
            degree = int(obj.degree)
        print(obj.coeff, 'X^', obj.degree)

    print("Polynomial degree:", degree)
    if degree > 2:
        raise SystemExit("The polynomial degree is stricly greater than 2, I can't solve.")


def main():
    data = read_input()
    left_data, right_data = parse_input(data)
    # data_parsed = parse_input(data)
    # left_data = left_side(data_parsed[0])
    # right_data = right_side(data_parsed[1])
    cleaned_right_data = remove_empty_items(right_data)
    cleaned_left_data = remove_empty_items(left_data)
    print(cleaned_left_data)
    print(cleaned_right_data)

    equation_list = []

    equation_list = get_list_of_objects(cleaned_left_data, cleaned_right_data)
    equation_list.sort(key=sort_get_degree, reverse=True)

    #print (equation_list)
    # save_terms_left(cleaned_left_data)
    # save_terms_right(cleaned_right_data)
    # print("constant", calc_constants())
    # print("1st degree", calc_first_degree())
    # print("2nd degree", calc_second_degree())
    # print(square_root(25))
    #sort_list_by_degree()
    handle_int_or_float(equation_list)
    reduced_form(equation_list)
    handle_degree(equation_list)
    solve_equation(equation_list)


if __name__ == "__main__":
    main()
