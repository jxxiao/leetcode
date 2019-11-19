#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (34.90%)
# Likes:    1819
# Dislikes: 54
# Total Accepted:    140.3K
# Total Submissions: 401.4K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],
#                       ["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
#
#
#


# @lc code=start
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        maxA = 0
        left, right, height = [0] * col, [col] * col, [0] * col

        for i in range(row):
            cur_left, cur_right = 0, col
            for j in range(col):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1

            for j in range(col):
                if matrix[i][~j] == '1':
                    right[~j] = min(right[~j], cur_right)
                else:
                    right[~j] = col
                    cur_right = col + ~j

            for j in range(col):
                maxA = max(maxA, (right[j] - left[j]) * height[j])
        return maxA


matrix = [["0", "0", "0", "1", "0", "0", "0"],
          ["0", "0", "1", "1", "1", "0", "0"],
          ["0", "1", "1", "1", "1", "1", "0"]]

matrix_1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
Solution().maximalRectangle(matrix_1)

# @lc code=end
