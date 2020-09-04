#!/usr/bin/env python3

# "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

import sys

def parse_input(data):

	data = data.replace(" ", "").replace("^", "")
	data = data.split("=")
	left = data[0]
	right = data[1]
	print ("left " + left)
	print ("right " + right)

	coeffs = []
	degrees = []

	for i, n in enumerate(left):
		print(i, nbr)
		if nbr is 'X':
			coeffs.append(left[i - 2])
			degrees.append(left[i + 1])
	print (coeffs)
	print (degrees)
	return (data)

def read_input():

	arg = sys.argv[1] if len(sys.argv) > 1 else "somevalue"

	return arg

def main():

	data = read_input()
	data_parsed = parse_input(data)
	print (data_parsed)


if __name__ == "__main__":
    main()  