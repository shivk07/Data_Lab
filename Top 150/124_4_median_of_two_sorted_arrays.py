class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            maxLeft1 = nums1[i - 1] if i > 0 else float('-inf')
            minRight1 = nums1[i] if i < m else float('inf')

            maxLeft2 = nums2[j - 1] if j > 0 else float('-inf')
            minRight2 = nums2[j] if j < n else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) +
                            min(minRight1, minRight2)) / 2.0
                return float(max(maxLeft1, maxLeft2))

            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1