from ipaddress import v4_int_to_packed
import unittest
from unittest import result
import main


class TestMain(unittest.TestCase):

    def setUp(self):
        print('about to test a function')

    def test_add_num(self):
        test_param = 10
        result = main.add_num(test_param)
        self.assertEqual(result, 15)

    def test_add_num_2(self):
        test_param = 'shakdak'
        result = main.add_num(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_add_num_3(self):
        test_param = None
        result = main.add_num(test_param)
        self.assertEqual(result, 'please enter number')

    def test_add_num_4(self):
        test_param = ''
        result = main.add_num(test_param)
        self.assertEqual(result, 'please enter number')

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
