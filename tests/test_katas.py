import unittest
import katas
import random


class TestKatas(unittest.TestCase):
    def test_add(self):
        number = random.randrange(-4, 25)
        number2 = random.randrange(-10, 250)
        total = number + number2
        self.assertEqual(katas.add(number, number2), total)

    def test_multiply(self):
        number = random.randrange(-4, 25)
        number2 = random.randrange(-10, 250)
        total = number * number2
        self.assertEqual(katas.multiply(number, number2), total)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)
        self.assertRaises(ValueError, katas.power, 4, -5)
        self.assertRaises(ValueError, katas.power, 5, 0.52)

    def test_factorial(self):
        list_factorial = [
            1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800,
            39916800, 479001600, 6227020800, 87178291200, 1307674368000]
        for i, value in enumerate(list_factorial):
            self.assertEqual(katas.factorial(i), value)
            self.assertRaises(ValueError, katas.factorial, -5)

    def test_fibonacci(self):
        list_fibs = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
            233, 377, 610, 987, 1597, 2584, 4181, 6765,
            10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811,
            514229, 832040]
        for i, value in enumerate(list_fibs):
            self.assertEqual(katas.fibonacci(i), value)
            self.assertRaises(ValueError, katas.fibonacci, -5)


if __name__ == '__main__':
    unittest.main()
