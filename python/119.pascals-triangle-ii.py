'''
@Description:

@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-20 02:06:51
@LastEditors: jxxiao
@LastEditTime: 2020-02-20 02:23:04
'''
#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (46.91%)
# Likes:    637
# Dislikes: 188
# Total Accepted:    250.7K
# Total Submissions: 534.5K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex):
        result = [1]
        for i in range(rowIndex):
            result.insert(0, 0)
            for j in range(i+1):
                result[j] = result[j] + result[j+1]
        return result
# @lc code=end
