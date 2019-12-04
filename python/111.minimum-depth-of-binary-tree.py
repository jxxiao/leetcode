'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-04 21:32:44
@LastEditors: jxxiao
@LastEditTime: 2019-12-04 21:36:48
'''
#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.06%)
# Likes:    924
# Dislikes: 524
# Total Accepted:    345.1K
# Total Submissions: 952.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
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
# return its minimum depth = 2.
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
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)

# @lc code=end
