import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        r = 3
        expected = math.pi * r * r
        self.assertAlmostEqual(area(r), expected, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        r = 3
        expected = 2 * math.pi * r
        self.assertAlmostEqual(perimeter(r), expected, places=7)
