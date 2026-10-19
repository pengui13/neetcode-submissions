class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_idx = 0
        s = s.replace(' ','')
        right_idx = len(s)-1
        while left_idx < right_idx:
            print(left_idx,right_idx)
            if not s[left_idx].isalnum():
                left_idx+=1
                continue
            if not s[right_idx].isalnum():
                right_idx-=1
                continue
            if s[left_idx].lower() != s[right_idx].lower():
                return False
            left_idx += 1
            right_idx -= 1
        return True