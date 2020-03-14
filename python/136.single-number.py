'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-03-05 00:59:36
@LastEditors: jxxiao
@LastEditTime: 2020-03-05 01:22:00
'''
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (62.87%)
# Likes:    3504
# Dislikes: 140
# Total Accepted:    635.7K
# Total Submissions: 1M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
#
#

# @lc code=start
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)
# @lc code=end
