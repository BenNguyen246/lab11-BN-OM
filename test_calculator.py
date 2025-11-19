import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(6, 9), 15)

        self.assertEqual(calculator.add(-420, 420), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)

        self.assertEqual(calculator.sub(5, 2), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(2025, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 1 / 3)

        self.assertEqual(calculator.log(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.log(1, 10)

    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 5), 10)
        self.assertEqual(calculator.mul(5, 5), 25)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertEqual(calculator.div(100, 2), 50)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 3)
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 3)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertEqual(calculator.hypotenuse(1, 1), calculator.square_root(2))

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(4), 2)

        with self.assertRaises(ValueError):
            calculator.square_root(0)


if __name__ == "__main__":
    unittest.main()
