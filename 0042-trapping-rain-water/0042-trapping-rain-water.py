class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        ans = 0

        for i, v in enumerate(height):
            while s and height[s[-1]] < v:
                bottom = s.pop()

                if not s:
                    break

                h = min(v, height[s[-1]]) - height[bottom]
                w = i - s[-1] - 1
                ans += h * w

            s.append(i)

        return ans