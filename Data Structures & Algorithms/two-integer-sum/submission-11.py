class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add_dict = {}
        for key, value in enumerate(nums):
            add_dict[value] = key
        for i in range(len(nums)):
            add_target = target - nums[i]
            if add_dict.get(add_target, -1) >=0 and i != add_dict[add_target]:
                return [i,add_dict[add_target]]
            add_target = target