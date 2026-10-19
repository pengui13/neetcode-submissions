class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left != right:
            my_target = numbers[left] + numbers[right]
            if my_target > target:
                right -= 1
            elif my_target < target: 
                left += 1
            else:
                return [left+1, right+1]
            