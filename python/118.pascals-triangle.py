'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-20 01:27:28
@LastEditors: jxxiao
@LastEditTime: 2020-02-20 01:57:18
'''
#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (50.01%)
# Likes:    1063
# Dislikes: 88
# Total Accepted:    332.3K
# Total Submissions: 664.4K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#

# @lc code=start
class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        numList = [[1]]
        for i in range(1, numRows):
            tempList = []
            tempList.append(1)
            for j in range(1, i):
                tempList.append(numList[i-1][j-1] + numList[i-1][j])
            tempList.append(1)
            numList.append(tempList)
        return numList
# @lc code=end

print(Solution().generate(5))
