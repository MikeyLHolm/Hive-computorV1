#!/usr/bin/python3
import unittest
from src.degree import sort_get_degree
from src.object_related import TermObject


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


class TestGetDegree(unittest.TestCase):

    def setUp(self):
        self.obj1 = TermObject(2, 1)
        self.obj2 = TermObject(3, 2)

    def test_sort_get_degree(self):
        print('\ntest_sort_get_degree')
        self.assertEqual(sort_get_degree(self.obj1), 1)
        self.assertEqual(sort_get_degree(self.obj2), 2)

        self.obj1.degree = -12
        self.obj2.degree = 18283

        self.assertEqual(sort_get_degree(self.obj1), -12)
        self.assertEqual(sort_get_degree(self.obj2), 18283)

        self.obj1.degree = -0
        self.obj2.degree = 0

        self.assertEqual(sort_get_degree(self.obj1), -0)
        self.assertEqual(sort_get_degree(self.obj2), 0)
