'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-23 19:07:36
@LastEditors: jxxiao
@LastEditTime: 2020-02-24 17:00:40
'''
#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (32.26%)
# Likes:    2596
# Dislikes: 212
# Total Accepted:    274.1K
# Total Submissions: 849.1K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
# ⁠      1
# ⁠     / \
# ⁠    2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
# -10
# / \
# 9  20
# /  \
# 15   7
#
# Output: 42
#
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
    def maxPathSum(self, root: TreeNode) -> int:

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum
# @lc code=end
