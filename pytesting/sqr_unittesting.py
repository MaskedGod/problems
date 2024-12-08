from wrong_square import square
import unittest


class TestSquare(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_positive(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        self.assertEqual(square(4), 16)
        self.assertEqual(square(5), 25)

    def test_negative(self):
        self.assertEqual(square(-2), 4)
        self.assertEqual(square(-3), 9)

    def test_str(self):
        with self.assertRaises(TypeError):
            square('cat')


if __name__ == '__main__':
    unittest.main()