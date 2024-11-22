from math import floor

class Solution:
    def mySqrt(self, x: int) -> int:
        def f(c: float):
            return c ** 2 - x

        def f_d(c: float):
            return 2 * c

        def n_r(c: float):
            return c - (f(c) / f_d(c))

        init = x / 2 + 1

        for i in range(19):
            init = n_r(init)

        return floor(init)
