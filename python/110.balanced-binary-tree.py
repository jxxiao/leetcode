'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-04 18:03:31
@LastEditors: jxxiao
@LastEditTime: 2019-12-04 18:06:12
'''
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.92%)
# Likes:    1603
# Dislikes: 142
# Total Accepted:    377K
# Total Submissions: 894.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
#
# a binary tree in which the left and right subtrees of every node differ in
# height by no more than 1.
#
#
#
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
#
#
# Return false.
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
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0, 1
            l, res_l = dfs(root.left)
            r, res_r = dfs(root.right)
            if res_l and res_r and -1<=l-r<=1:
                res = 1
            else:
                res = 0
            return max(l,r)+1, res
        return dfs(root)[1] == 1

# @lc code=end
