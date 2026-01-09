from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)

    def test_moyenne(self):
        self.assertEqual(self.calc.moyenne([2, 4, 6]), 4.0)  # Note: float
        self.assertEqual(self.calc.moyenne([1]), 1.0)
    
    
if __name__ == '__main__':
    unittest.main()