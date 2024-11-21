class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N, d, left = len(s), {}, 0

        ans = 0

        for right in range(N):
            d[s[right]] = d.get(s[right], 0) + 1

            while left < right and right - left + 1 != len(d.keys()):
                d[s[left]] -= 1
                if d[s[left]] == 0:
                    del d[s[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans