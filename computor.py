#!/usr/bin/env python3
import sys
from src.solver import solve


def main():
    try:
        solve()
    except KeyboardInterrupt:
        print('\nKeyboardInterrupt handled')


if __name__ == "__main__":
    main()
