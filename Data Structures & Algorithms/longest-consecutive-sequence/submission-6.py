class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ordered_list = sorted(set(nums))
        counter = 1
        counter_list = list()
        if not len(nums):
            return 0
        prev_number = ordered_list[0]
        for elem in ordered_list:
            diff = elem - prev_number
            if diff == 1:
                counter += 1
            else:
                counter_list.append(counter)
                counter = 1
            prev_number = elem
        counter_list.append(counter)
        return max(counter_list)
        