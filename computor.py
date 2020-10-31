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
from src.solver import solve


def main():
    solve()


if __name__ == "__main__":
    main()
