class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        for el in strs:
            key = "".join(sorted(el))
            if key not in strs_dict:
                strs_dict[key] = [el]
            else:
                strs_dict[key].append(el)
        return list(strs_dict.values())