from math import floor

class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return 1

        left = 0

        right = x

        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 > x:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1

        return ans
