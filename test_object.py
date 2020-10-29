#!/usr/bin/python3
import unittest
from object_related import TermObject, opposite_sign


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


class TestCoolFunction(unittest.TestCase):

    def test_opposite_sign(self):
        print('\ntest_opposite_sign')
        self.assertEqual(opposite_sign('-9'), '9')
        self.assertEqual(opposite_sign('-0'), '0')
        self.assertEqual(opposite_sign('0'), '0')


if __name__ == '__main__':
    unittest.main()
