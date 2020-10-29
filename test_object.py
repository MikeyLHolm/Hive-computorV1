#!/usr/bin/python3
import unittest
from object_related import TermObject

class TestTermObject(unittest.TestCase):

    def setUp(self):
        self.obj1 = TermObject(2, 1)
        self.obj2 = TermObject(3, 2)

    def test_coefficient(self):
        print('\ntest_coefficient')
        self.assertEqual(self.obj1.coeff, 2)
        self.assertEqual(self.obj2.coeff, 3)

        self.obj1.coeff = -54
        self.obj2.coeff = 0

        self.assertEqual(self.obj1.coeff, -54)
        self.assertEqual(self.obj2.coeff, 0)

    def test_degree(self):
        print('\ntest_degree')
        self.assertEqual(self.obj1.degree, 1)
        self.assertEqual(self.obj2.degree, 2)

        self.obj1.degree = 0
        self.obj2.degree = 1

        self.assertEqual(self.obj1.degree, 0)
        self.assertEqual(self.obj2.degree, 1)

if __name__ == '__main__':
    unittest.main()