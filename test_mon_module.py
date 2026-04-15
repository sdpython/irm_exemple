import unittest

from mon_module import une_fonction

class TestMonModule(unittest.TestCase):
    def test_une_function(self):
        self.assertEqual(une_fonction(4 , 5), 9)

if __name__ == "__main__":
    unittest.main()