class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').replace('?', '').replace(',', '').replace("'", '').replace(".", '').replace(":", '').replace("!", '').lower()
        return s == s[::-1]