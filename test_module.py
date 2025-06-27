import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate_correct(self):
        self.assertEqual(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]), {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666]*3, 6.666666666666667],
            'standard deviation': [[2.449489742783178]*3, [0.816496580927726]*3, 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        })

    def test_calculate_raises_error(self):
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")

if __name__ == "__main__":
    unittest.main()
