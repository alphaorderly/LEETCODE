class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(text: str) -> bool:
            return text == text[::-1]

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_palindrome(s[left:right]) or is_palindrome(s[left + 1: right + 1])

        return True