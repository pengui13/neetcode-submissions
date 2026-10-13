class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for el in nums:
            my_set.add(el)
        return len(my_set) != len(nums)