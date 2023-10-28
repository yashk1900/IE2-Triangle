import unittest
from isTriangle import Triangle


class TriangleTest(unittest.TestCase):
    INVALID = 0
    SCALENE = 1
    EQUILATERAL = 2
    ISOSCELES = 3
    def test_invalid1(self):
        self.assertEqual(Triangle.classify(0, 0, -1), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(0, -4, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 0, -4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-4, 5, 0), Triangle.Type.INVALID)

    def test_invalid2(self):
        self.assertEqual(Triangle.classify(10, 2, 13), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(9, 10, -2), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(2, 13, 10), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 3, 10), Triangle.Type.INVALID)

    def test_invalid3(self):
        self.assertEqual(Triangle.classify(5, 5, 12), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(5, 12, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(12, 5, 5), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(-1, 4, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, -1, 4), Triangle.Type.INVALID)
        self.assertEqual(Triangle.classify(4, 4, -1), Triangle.Type.INVALID)

    def test_equilateral(self):
        self.assertEqual(Triangle.classify(5, 5, 5), Triangle.Type.EQUILATERAL)

    def test_isosceles(self):
        self.assertEqual(Triangle.classify(5, 5, 4), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(5, 4, 5), Triangle.Type.ISOSCELES)
        self.assertEqual(Triangle.classify(4, 5, 5), Triangle.Type.ISOSCELES)

    def test_scalene(self):
        self.assertEqual(Triangle.classify(5, 11, 7), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(7, 5, 11), Triangle.Type.SCALENE)
        self.assertEqual(Triangle.classify(11, 7, 5), Triangle.Type.SCALENE)


if __name__ == '__main__':
    unittest.main()