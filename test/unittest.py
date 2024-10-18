import unittest

from SmartCityTraffic import find_busiest_intersections

class TestFindBusiestIntersections(unittest.TestCase):
    def test_single_busiest(self):
        intersections = {
            "A": 100,
            "B": 200,
            "C": 150
        }
        result = find_busiest_intersections(intersections)
        self.assertEqual(result, ["B"])

    def test_multiple_busiest(self):
        intersections = {
            "A": 300,
            "B": 200,
            "C": 300
        }
        result = find_busiest_intersections(intersections)
        self.assertCountEqual(result, ["A", "C"])

    def test_no_intersections(self):
        intersections = {}
        result = find_busiest_intersections(intersections)
        self.assertEqual(result, [])

    def test_all_same(self):
        intersections = {
            "A": 100,
            "B": 100,
            "C": 100
        }
        result = find_busiest_intersections(intersections)
        self.assertCountEqual(result, ["A", "B", "C"])

if __name__ == '__main__':
    unittest.main()
