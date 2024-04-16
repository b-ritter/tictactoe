import unittest

class TestView(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()