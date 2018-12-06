import unittest
from day_5 import day_5_1, day_5_2

class Day5Tests(unittest.TestCase):
    def day_5_1_test(self):
        self.assertEqual(day_5_1("day_5_test_input.txt"), 10)
    def day_5_2_test(self):
        self.assertEqual(day_5_2("day_5_test_input.txt"), 4)
