import unittest
from isTriangle import Triangle


class TriangleTest(unittest.TestCase):

    def test_invalid(self):
        actual = Triangle.classify(0, -4, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)
        actual1 = Triangle.classify(4, 5, 11)
        expected1 = Triangle.Type.INVALID
        self.assertEqual(actual1, expected1)
        actual2 = Triangle.classify(11, 4, 5)
        expected2 = Triangle.Type.INVALID
        self.assertEqual(actual2, expected2)
        actual3 = Triangle.classify(5, 11, 4)
        expected3 = Triangle.Type.INVALID
        self.assertEqual(actual3, expected3)

    def test_eqiulateral(self):
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def test_isosceles(self):
        actual = Triangle.classify(4, 4, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        actual1 = Triangle.classify(5, 4, 4)
        expected1 = Triangle.Type.ISOSCELES
        self.assertEqual(actual1, expected1)
        actual2 = Triangle.classify(4, 5, 4)
        expected2 = Triangle.Type.ISOSCELES
        self.assertEqual(actual2, expected2)

    def test_scalene(self):
        actual = Triangle.classify(4,5,10)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)