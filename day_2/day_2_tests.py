import unittest
from day_2 import day_2_1, day_2_2

class Day2Tests(unittest.TestCase):
    def day_2_1_test(self):
        self.assertEqual(day_2_1("day_2_1_test_input.txt"), 12)
    def day_2_2_test(self):
        self.assertEqual(day_2_2("day_2_2_test_input.txt"), "fgij")