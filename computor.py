#!/usr/bin/env python3

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0 - 3 * X^2"
# import re
import sys

constants = []
x_1 = []
x_2 = []


def read_input():
    arg = sys.argv[1] if len(sys.argv) > 1 else "somevalue"
    return arg


# Function to return the square root of
# a number using Newtons method
def square_root(n):

    # Setting tolerance level
    tolerance_level = 0.00001

    # Assuming the sqrt of n as n only
    x = n

    # To count the number of iterations
    count = 0

    while (1):
        count += 1

        # Calculate more closed x
        root = 0.5 * (x + (n / x))

        # Check for closeness
        if (abs(root - x) < tolerance_level):
            break

        # Update root
        x = root

    return root


def parse_input(data):
    data = data.replace(" ", "").replace("^", "").replace("-", "+-")
    data = data.split("=")
    # left = data[0]
    # right = data[1]

    # coeffs = []
    # degrees = []

    # for i, nbr in enumerate(left):
    #     print(i, nbr)
    #     if nbr == 'X':
    #         coeffs.append(left[i - 2])
    #         degrees.append(left[i + 1])
    #         print(coeffs)
    #         print(degrees)

    return (data)


def left_side(left):
    print("left " + left)
    terms = left.split('+')
    # terms = [x.strip() for x in terms]
    # print("terms are: " + terms)
    return terms


def right_side(right):
    print("right " + right)
    terms = right.split('+')
    return terms


def sort_terms(left, right):
    print("L terms are: ", left)
    print("R terms are: ", right)

    for term in left:
        if term.find('X') is not -1:
            print(term)
            for i, c in enumerate(term):
                if c == 'X':
                    print(c)
                    print(term[i + 1])
                    if term[i + 1] == '0':
                        constants.append(term[0:i - 1])
                    elif term[i + 1] == '1':
                        x_1.append(term[0:i - 1])
                    elif term[i + 1] == '2':
                        x_2.append(term[0:i - 1])
                    else:
                        sys.exit('Other degrees not supported, EXIT')
        else:
            sys.exit('No X in a term, EXIT')


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


def main():
    data = read_input()
    data_parsed = parse_input(data)
    # print(data_parsed)
    left_data = left_side(data_parsed[0])
    right_data = right_side(data_parsed[1])
    cleaned_right_data = remove_empty_items(right_data)
    cleaned_left_data = remove_empty_items(left_data)
    sort_terms(cleaned_left_data, cleaned_right_data)
    print('constant', calc_constants())
    print('1st degree', calc_first_degree())
    print('2nd degree', calc_second_degree())
    # print(square_root(25))


if __name__ == "__main__":
    main()
