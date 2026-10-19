class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        sol_list = []
        for static in range(len(nums)):
            static_number = nums[static]
            left = static + 1
            right = len(nums) - 1
            target = (-1) * static_number
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    if [static_number, nums[left], nums[right]] not in sol_list:
                        sol_list.append([static_number, nums[left], nums[right]])
                    left += 1
                    right -= 1
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
        return sol_list