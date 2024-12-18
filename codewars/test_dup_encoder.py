import unittest
from dup_encoder import duplicate_encode


class TestEncode(unittest.TestCase):

    def test_lower(self):
        self.assertEqual(duplicate_encode("din"), "(((")
        self.assertEqual(duplicate_encode("recede"), "()()()")

    def test_capitalized(self):
        self.assertEqual(duplicate_encode("Success"), ")())())")

    def test_symbols(self):
        self.assertEqual(duplicate_encode("(( @"), "))((")


if __name__ == "__main__":
    unittest.main()
