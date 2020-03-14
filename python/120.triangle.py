'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-20 22:14:55
@LastEditors: jxxiao
@LastEditTime: 2020-02-21 01:47:34
'''

#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (42.24%)
# Likes:    1573
# Dislikes: 187
# Total Accepted:    221.5K
# Total Submissions: 524.2K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#


# @lc code=start
class Solution:
    def minimumTotal(self, triangle):
        minlen = list(triangle[-1])
        for layer in range(len(triangle) - 2, -1, -1):
            for i in range(layer+1):
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]
        return minlen[0]


nums = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
Solution().minimumTotal(nums)

# @lc code=end
