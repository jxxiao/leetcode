'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-03-05 01:42:21
@LastEditors: jxxiao
@LastEditTime: 2020-03-05 16:02:32
'''

#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (48.44%)
# Likes:    1217
# Dislikes: 307
# Total Accepted:    196.9K
# Total Submissions: 405.5K
# Testcase Example:  '[2,2,3,2]'
#
# Given a non-empty array of integers, every element appears three times except
# for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,3,2]
# Output: 3
#
#
# Example 2:
#
#
# Input: [0,1,0,1,0,1,99]
# Output: 99
#
#


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for num in nums:
            one = (one ^ num) & ~two
            two = (two ^ num) & ~one
        return one


# @lc code=end
