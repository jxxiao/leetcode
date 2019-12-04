'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-04 23:30:19
@LastEditors: jxxiao
@LastEditTime: 2019-12-04 23:37:08
'''
#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (38.96%)
# Likes:    1260
# Dislikes: 396
# Total Accepted:    378.4K
# Total Submissions: 963.7K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = []
        self.dfs(root, sum, res)
        return any(res)
    def dfs(self, root, target, res):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)
# @lc code=end
