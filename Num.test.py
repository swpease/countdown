import unittest

from Num import Num


class TestNum(unittest.TestCase):
    def setUp(self) -> None:
        self.lo = Num(2, 0)
        self.hi = Num(10, 1)
        self.odd = Num(3, 2)
        self.overlap = Num(3, 2)

    def test_add(self):
        result = self.lo + self.hi
        self.assertEqual(result.value, 12, "adds")
        self.assertEqual(result.math_path, "(2 + 10)", "path")
        self.assertEqual(result.base_indexes, self.lo.base_indexes | self.hi.base_indexes, "source kept")

    def test_subtract(self):
        result = self.lo - self.hi
        result2 = self.hi - self.lo
        self.assertEqual(result.value, 8, "subtracts")
        self.assertEqual(result2.value, 8, "subtracts")
        self.assertEqual(result.math_path, "(10 - 2)", "path")
        self.assertEqual(result2.math_path, "(10 - 2)", "path")
        self.assertEqual(result.base_indexes, self.lo.base_indexes | self.hi.base_indexes, "source kept")

    def test_multiply(self):
        result = self.lo * self.hi
        self.assertEqual(result.value, 20, "multiplies")
        self.assertEqual(result.math_path, "(2 * 10)", "path")
        self.assertEqual(result.base_indexes, self.lo.base_indexes | self.hi.base_indexes, "source kept")

    def test_divide(self):
        result = self.hi // self.lo
        result2 = self.hi // self.odd
        self.assertEqual(result.value, 5, "divides")
        self.assertIsNone(result2, "only handles whole division")
        self.assertEqual(result.math_path, "(10 / 2)", "path")
        self.assertEqual(result.base_indexes, self.lo.base_indexes | self.hi.base_indexes, "source kept")

    def test_combine(self):
        indivisible = [self.odd + self.hi, self.odd - self.hi, self.odd * self.hi]
        indiv_vals = [num.value for num in indivisible]
        real_indivisble = Num.combine(self.odd, self.hi)
        real_indiv_vals = [num.value for num in real_indivisble]
        self.assertEqual(indiv_vals, real_indiv_vals, "omits faulty division")

        divisible = [self.lo + self.hi, self.lo - self.hi, self.lo * self.hi, self.lo // self.hi]
        div_vals = [num.value for num in divisible]
        real_divisble = Num.combine(self.lo, self.hi)
        real_div_vals = [num.value for num in real_divisble]
        self.assertEqual(div_vals, real_div_vals, "does all four operations")

    def test_disjoint(self):
        self.assertFalse(Num.is_disjoint(self.odd, self.overlap))
        self.assertTrue(Num.is_disjoint(self.lo, self.hi))


if __name__ == '__main__':
    unittest.main()
