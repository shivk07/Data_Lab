class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]

    def binSearch(self, nums, target, left):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                i = mid
                if left:
                    r = mid - 1
                else: 
                    l = mid + 1
        return i