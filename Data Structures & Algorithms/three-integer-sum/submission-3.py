class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol_list = []
        for static in range(len(nums)):
            if static > 0 and nums[static] == nums[static - 1]:
                continue  
            static_number = nums[static]
            left = static + 1
            right = len(nums) - 1
            target = (-1) * static_number
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    sol_list.append([static_number, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
        return sol_list