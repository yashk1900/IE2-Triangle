import unittest
from isTriangle import Triangle

class TriangleTest(unittest.TestCase):

    def test_invalid1(self):
        actual0 = Triangle.classify(5, 0, 5)
        expected0 = Triangle.Type.INVALID
        self.assertEqual(actual0,expected0)

    def test_invalid2(self):
        actual1 = Triangle.classify(5, 5, 10)
        expected1 = Triangle.Type.INVALID
        self.assertEqual(actual1, expected1)

    def test_invalid3(self):
        actual2 = Triangle.classify(5, 10, 5)
        expected2 = Triangle.Type.INVALID
        self.assertEqual(actual2, expected2)

    def test_invalid4(self):
        actual3 = Triangle.classify(10, 5, 5)
        expected3 = Triangle.Type.INVALID
        self.assertEqual(actual3, expected3)

    def test_invalid5(self):
        actual4 = Triangle.classify(10, 5, 4)
        expected4 = Triangle.Type.INVALID
        self.assertEqual(actual4, expected4)

    def testScalene(self):
        actual = Triangle.classify(10, 5, 6)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testEquilateral(self):
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testIsosceles(self):
        actual = Triangle.classify(5, 5, 9)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)
        actual1 = Triangle.classify(5, 9, 5)
        expected1 = Triangle.Type.ISOSCELES
        self.assertEqual(actual1, expected1)
        actual2 = Triangle.classify(9, 5, 5)
        expected2 = Triangle.Type.ISOSCELES
        self.assertEqual(actual2, expected2)