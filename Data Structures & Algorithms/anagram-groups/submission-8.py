from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for el in strs:
            key = ''.join(sorted(el))
            groups[key].append(el)
        return list(groups.values())