from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = defaultdict(list)
        for el in strs:
            key = "".join(sorted(el))
            strs_dict[key].append(el)
        return list(strs_dict.values())