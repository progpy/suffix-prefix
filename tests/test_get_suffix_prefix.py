import unittest

from suffix_prefix.suffix_prefix import find_suffix_prefix


class TestSuffixPrefix(unittest.TestCase):
    def test_empty_data(self):
        result = find_suffix_prefix([])
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
