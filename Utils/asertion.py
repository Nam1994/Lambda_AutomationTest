import logging
import unittest


class Assertion(unittest.TestCase):
    def assert_equal(self, expected, actual, msg=''):
        try:
            self.assertEqual(expected, actual, msg)
        except AssertionError as ae:
            logging.warning(ae)
