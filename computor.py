#!/usr/bin/env python3

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
# import re
import sys


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
    print("terms are: ", terms)
    # terms = [x.strip() for x in terms]
    # print("terms are: " + terms)


def right_side(right):
    print("right " + right)


def read_input():
    arg = sys.argv[1] if len(sys.argv) > 1 else "somevalue"
    return arg


def main():
    data = read_input()
    data_parsed = parse_input(data)
    print(data_parsed)
    left_side(data_parsed[0])
    right_side(data_parsed[1])
    print(square_root(25))


if __name__ == "__main__":
    main()
