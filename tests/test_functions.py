import unittest
from src.int_or_float import str_to_float_or_int
from src.object_related import opposite_sign


class TestCoolFunction(unittest.TestCase):

    def test_opposite_sign(self):
        print('\ntest_opposite_sign')
        self.assertEqual(opposite_sign('-9'), '9')
        self.assertEqual(opposite_sign('-0'), '0')
        self.assertEqual(opposite_sign('0'), '0')


    def test_str_to_float_or_int(self):
        print('\ntest_str_to_float_or_int')
        self.assertIsInstance(str_to_float_or_int('0.81823'), float)
        self.assertIsInstance(str_to_float_or_int('-123.1'), float)
        self.assertIsInstance(str_to_float_or_int('0.000001'), float)
        self.assertIsInstance(str_to_float_or_int('-0.000001'), float)
        self.assertIsInstance(str_to_float_or_int('-0'), int)
        self.assertIsInstance(str_to_float_or_int('0'), int)
        self.assertIsInstance(str_to_float_or_int('-0.00'), int)
        self.assertIsInstance(str_to_float_or_int('-0.00000000'), int)
        self.assertIsInstance(str_to_float_or_int('-123.00000000'), int)
        self.assertIsInstance(str_to_float_or_int('6'), int)

