class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for el in s:
            if el not in s_dict:
                s_dict[el] = 0
            s_dict[el] += 1
        for el in t:
            if el not in t_dict:
                t_dict[el] = 0
            t_dict[el] += 1
        return s_dict == t_dict