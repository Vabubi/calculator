import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Create a new Calculator instance before each test."""
        self.calc = Calculator()

    def test_addition(self):
        """Test adding numbers."""
        self.assertEqual(self.calc.add(5), 5.0)
        self.assertEqual(self.calc.add(3), 8.0)

    def test_subtraction(self):
        """Test subtracting numbers."""
        self.calc.add(10)
        self.assertEqual(self.calc.subtract(4), 6.0)

    def test_multiplication(self):
        """Test multiplying numbers."""
        self.calc.add(2)
        self.assertEqual(self.calc.multiply(3), 6.0)

    def test_division(self):
        """Test dividing numbers."""
        self.calc.add(10)
        self.assertEqual(self.calc.divide(2), 5.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        self.calc.add(10)
        with self.assertRaises(ValueError):
            self.calc.divide(0)

    def test_nth_root(self):
        """Test nth root calculation."""
        self.calc.add(16)
        self.assertAlmostEqual(self.calc.nth_root(2), 4.0)

    def test_reset(self):
        """Test resetting memory to 0."""
        self.calc.add(10)
        self.calc.reset()
        self.assertEqual(self.calc.memory, 0.0)

if __name__ == '__main__':
    unittest.main()
