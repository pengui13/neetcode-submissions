class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_number = 100
        max_diff = 0
        for el in prices:
            min_number = el if el <= min_number else min_number
            diff = el - min_number
            max_diff = diff if diff > max_diff else max_diff
        return max_diff