#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (37.18%)
# Likes:    1401
# Dislikes: 3219
# Total Accepted:    443.2K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
# Note:
#
#
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
#
#
# Example:
#
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#
#


# @lc code=start
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l1, l2, last = m - 1, n - 1, m + n - 1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[last] = nums2[l2]
                l2 -= 1
            else:
                nums1[last] = nums1[l1]
                l1 -= 1
            last -= 1
        if l1 < 0:
            nums1[:l2 + 1] = nums2[:l2 + 1]


# @lc code=end
