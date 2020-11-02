import unittest
from src.degree import handle_degree
from src.handle_complex_input import handle_no_coeff, handle_no_degree, handle_zero_degree_form
from src.int_or_float import str_to_float_or_int
from src.object_related import opposite_sign, TermObject
from src.square_root import square_root


class TestDegree(unittest.TestCase):

    def setUp(self):
        self.object_list = []
        self.obj1 = TermObject(2, 1)
        self.obj2 = TermObject(3, 2)
        self.obj3 = TermObject(0, 5)
        self.obj4 = TermObject(-3, 1)
        self.object_list.append(self.obj1)
        self.object_list.append(self.obj2)
        self.object_list.append(self.obj3)
        self.object_list.append(self.obj4)


    def test_list_object(self):
        print('\ntest_list_object')
        self.assertEqual(self.object_list[0].coeff, 2)
        self.assertEqual(self.object_list[0].degree, 1)
        self.assertEqual(self.object_list[1].coeff, 3)
        self.assertEqual(self.object_list[1].degree, 2)
        self.assertEqual(self.object_list[2].coeff, 0)
        self.assertEqual(self.object_list[2].degree, 5)
        self.assertEqual(self.object_list[3].coeff, -3)
        self.assertEqual(self.object_list[3].degree, 1)


    def test_handle_degree(self):
        print('\ntest_handle_degree')
        with self.assertRaises(SystemExit) as cm:
            handle_degree(self.object_list)
        error_message = cm.exception.args[0]
        self.assertEqual('The polynomial degree is stricly greater than 2, I can\'t solve.', error_message)

        self.object_list[2].degree = 0

        self.assertEqual(handle_degree(self.object_list), 2)

        self.object_list[0].degree = -10
        self.object_list[1].degree = -32
        self.object_list[2].degree = -1
        self.object_list[3].degree = 0

        with self.assertRaises(SystemExit) as cm:
            handle_degree(self.object_list)
        error_message = cm.exception.args[0]
        self.assertEqual('The polynomial degree is smaller than 1, I can\'t solve. Check your equation!', error_message)


class TestIntOrFloat(unittest.TestCase):

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


class TestHandleComplexInput(unittest.TestCase):

    def setUp(self):
        self.object_list1 = ['3', '-2*X2', '4*X1']
        self.object_list2 = ['-2', '6*X2', '14*X1']


    def test_handle_zero_degree_form(self):
        print('\ntest_handle_zero_degree_form')
        left_return, right_return = handle_zero_degree_form(self.object_list1, self.object_list2)
        self.assertEqual(left_return, ['3*X0', '-2*X2', '4*X1'])
        self.assertEqual(right_return, ['-2*X0', '6*X2', '14*X1'])

        self.object_list1[0] = '0'
        self.object_list2[0] = '-0'

        left_return, right_return = handle_zero_degree_form(self.object_list1, self.object_list2)
        self.assertEqual(left_return, ['0*X0', '-2*X2', '4*X1'])
        self.assertEqual(right_return, ['-0*X0', '6*X2', '14*X1'])


    def test_handle_no_coeff(self):
        print('\ntest_handle_no_coeff')

        self.object_list1[0] = 'X0'
        self.object_list1[1] = 'X1'
        self.object_list1[2] = '-X2'
        self.object_list2[0] = 'X2'
        self.object_list2[1] = '-X1'
        self.object_list2[2] = '-X0'

        left_return, right_return = handle_no_coeff(self.object_list1, self.object_list2)
        self.assertEqual(left_return, ['1*X0', '1*X1', '-1*X2'])
        self.assertEqual(right_return, ['1*X2', '-1*X1', '-1*X0'])


    def test_handle_no_degree(self):
        print('\ntest_handle_no_degree')

        self.object_list1[0] = '12*X0'
        self.object_list1[1] = '6*X'
        self.object_list1[2] = '-2*X2'
        self.object_list2[0] = '5*X2'
        self.object_list2[1] = '-5*X'
        self.object_list2[2] = '-8*X0'

        left_return, right_return = handle_no_degree(self.object_list1, self.object_list2)
        self.assertEqual(left_return, ['12*X0', '6*X1', '-2*X2'])
        self.assertEqual(right_return, ['5*X2', '-5*X1', '-8*X0'])

        self.object_list1[1] = '0*X'
        self.object_list2[1] = '-0*X'

        left_return, right_return = handle_no_degree(self.object_list1, self.object_list2)
        self.assertEqual(left_return, ['12*X0', '0*X1', '-2*X2'])
        self.assertEqual(right_return, ['5*X2', '-0*X1', '-8*X0'])


class TestMathFunctions(unittest.TestCase):

    def test_opposite_sign(self):
        print('\ntest_opposite_sign')
        self.assertEqual(opposite_sign('-9'), '9')
        self.assertEqual(opposite_sign('-0'), '0')
        self.assertEqual(opposite_sign('0'), '0')


    def test_square_root(self):
        print('\ntest_square_root')
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(625), 25)
        self.assertEqual(round(square_root(8), 6), 2.828427)
        self.assertEqual(round(square_root(12.6), 6), 3.549648)

        with self.assertRaises(SystemExit) as cm:
            square_root(-25)
        error_message = cm.exception.args[0]
        self.assertEqual('n is smaller than 0. Can\'t solve sqrt.', error_message)


def reduced_form(object_list):
            if not object_list:
                raise SystemExit('Reduced form: 0 = 0. All real numbers are the solution')

            reduced_form = 'Reduced form: ' + str(round(object_list[0].coeff, 6)) + ' * X^' + str(object_list[0].degree)

            for term in object_list[1:]:
                sign = ' + '
                if float(term.coeff) < 0:
                    sign = ' - '
                reduced_form = reduced_form + sign + str(round(term.coeff, 6)).strip('-') + ' * X^' + str(term.degree)

            reduced_form = reduced_form + ' = 0'
            return(reduced_form)


class TestReducedForm(unittest.TestCase):

    def setUp(self):
        self.object_list1 = []
        self.object_list2 = []
        self.object1 = TermObject(-8343.1273123, 1)
        self.object2 = TermObject(-0.5441300000000098, 0)
        self.object_list1.append(self.object1)
        self.object_list1.append(self.object2)
        self.object3 = TermObject(-6.99, 2)
        self.object4 = TermObject(13.04, 1)
        self.object5 = TermObject(7.99, 0)
        self.object_list2.append(self.object3)
        self.object_list2.append(self.object4)
        self.object_list2.append(self.object5)


    def test_reduced_form(self):
        self.assertEqual(reduced_form(self.object_list1), 'Reduced form: -8343.127312 * X^1 - 0.54413 * X^0 = 0')
        self.assertEqual(reduced_form(self.object_list2), 'Reduced form: -6.99 * X^2 + 13.04 * X^1 + 7.99 * X^0 = 0')
