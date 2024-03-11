import unittest


class TestStringMethods(unittest.TestCase):
    # First test case
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # Second Test case
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertFalse('c0d!ng'.isalnum())

    # Third Test case
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # Check s.index failed when not found
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    # Test Runner
    unittest.main()
