import unittest
from mutant import Mutant

class TestMutant(unittest.TestCase):
    def test_use_power(self):
        m = Mutant("Test", "Invisibility", 3)
        self.assertIn("uses", m.use_power())

if __name__ == "__main__":
    unittest.main()
