class Num(object):

    def __init__(self, value, base_indexes, math_path=None):
        self.value = value
        self.base_indexes = base_indexes if isinstance(base_indexes, frozenset) else frozenset([base_indexes])
        self.math_path = math_path if math_path is not None else str(value)

    def __add__(self, other):
        added = self.value + other.value
        math_path = "({} + {})".format(self, other)
        base_indexes = self.base_indexes | other.base_indexes
        return Num(added, base_indexes, math_path)

    def __sub__(self, other):
        small, big = (self, other) if self.value < other.value else (other, self)
        diff = big.value - small.value
        math_path = "({} - {})".format(big, small)
        base_indexes = self.base_indexes | other.base_indexes
        return Num(diff, base_indexes, math_path)

    def __mul__(self, other):
        prod = self.value * other.value
        math_path = "({} * {})".format(self, other)
        base_indexes = self.base_indexes | other.base_indexes
        return Num(prod, base_indexes, math_path)

    def __floordiv__(self, other):
        numerator, denominator = (self, other) if self.value < other.value else (other, self)
        if denominator.value == 0 or numerator.value == 0 or denominator.value % numerator.value != 0:
            return
        else:
            div = denominator.value // numerator.value
            math_path = "({} / {})".format(denominator, numerator)
            base_indexes = denominator.base_indexes | numerator.base_indexes
            return Num(div, base_indexes, math_path)

    def __str__(self):
        return self.math_path

    @staticmethod
    def combine(a, b):
        results = [a + b, a - b, a * b]
        div = a // b
        if div is not None:
            results.append(div)
        return results

    @staticmethod
    def is_disjoint(a, b):
        return a.base_indexes.isdisjoint(b.base_indexes)
