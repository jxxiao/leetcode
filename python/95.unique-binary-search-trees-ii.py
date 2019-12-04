'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-27 20:03:34
@LastEditors: jxxiao
@LastEditTime: 2019-11-27 21:07:44
'''
#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (37.31%)
# Likes:    1609
# Dislikes: 133
# Total Accepted:    160.3K
# Total Submissions: 426K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
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
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        res = self.dfs(1, n)
        return [] if res == [None] else res

    def dfs(self, l, r):
        res = []
        if r < l:
            res.append(None)
            return res

        for m in range(l, r + 1):
            left = self.dfs(l, m - 1)
            right = self.dfs(m + 1, r)
            for lNode in range(0, len(left)):
                for rNode in range(0, len(right)):
                    new = TreeNode(m)
                    new.left = left[lNode]
                    new.right = right[rNode]
                    res.append(new)
        return res


print(Solution().generateTrees(0))

# @lc code=end
