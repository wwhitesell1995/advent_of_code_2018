import unittest
from day_11 import day_11_1, get_fuel_cell_list, day_11_2

class Day11Tests(unittest.TestCase):
    def day_11_1_test(self):
        self.assertEqual(get_fuel_cell_list(8)[2][4], 4)
        self.assertEqual(get_fuel_cell_list(57)[121][78], -5)
        self.assertEqual(day_11_1(18), [33, 45])
        self.assertEqual(day_11_1(42), [21, 61])
    def day_11_2_test(self):
        self.assertEqual(day_11_2(18), [90, 269, 16])
