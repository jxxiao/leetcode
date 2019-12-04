'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-27 21:10:01
@LastEditors: jxxiao
@LastEditTime: 2019-11-27 21:26:09
'''
#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (48.20%)
# Likes:    2287
# Dislikes: 87
# Total Accepted:    234.4K
# Total Submissions: 481.9K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        G = [0 for i in range(n+1)]
        G[0] = G[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i - j]
        return G[n]
# @lc code=end
