import unittest
from day_1 import find_total_frequency, find_duplicate_frequency

class FrequencyTest(unittest.TestCase):
    def day_1_1_test(self):
        self.assertEqual(find_total_frequency("day_1_test_input.txt"), 3)
    def day_1_2_test(self):
        self.assertEqual(find_duplicate_frequency("day_1_test_input.txt"), 2)