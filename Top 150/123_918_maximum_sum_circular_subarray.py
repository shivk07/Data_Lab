class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max = 0
        curr_min = 0
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
            curr_min = min(num, curr_min + num)
            min_sum = min(min_sum, curr_min)
            total += num
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)