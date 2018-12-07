import unittest
from day_4 import day_4_1, day_4_2

class Day4Tests(unittest.TestCase):
    def day_4_1_test(self):
        self.assertEqual(day_4_1("day_4_test_input.txt"), 240)
    def day_4_2_test(self):
        self.assertEqual(day_4_2("day_4_test_input.txt"), 4455)
