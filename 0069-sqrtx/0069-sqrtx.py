from math import floor

class Solution:
    def mySqrt(self, x: int) -> int:
        def f(c: float):
            return c ** 2 - x

        def f_d(c: float):
            return 2 * c

        def n_r(c: float):
            return c - (f(c) / f_d(c))

        prev = x / 2 + 1
        init = x / 2 + 1

        for i in range(20):
            prev = init
            init = n_r(init)
            if abs(((init - prev) / init) * 100.0) < 0.0005:
                break

        return floor(init)
        