class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for el in s:
            s_dict[el] = s_dict.get(el, 0) + 1
        for el in t:
            if el not in t_dict:
                t_dict[el] = 0
            t_dict[el] += 1
        return s_dict == t_dict