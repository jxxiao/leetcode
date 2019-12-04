'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-03 23:47:51
@LastEditors: jxxiao
@LastEditTime: 2019-12-03 23:49:26
'''
#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (62.55%)
# Likes:    1737
# Dislikes: 61
# Total Accepted:    636.5K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(map(self.maxDepth,(root.left, root.right))) if root else 0
# @lc code=end
