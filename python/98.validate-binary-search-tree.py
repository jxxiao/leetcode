#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (26.49%)
# Likes:    2679
# Dislikes: 388
# Total Accepted:    520.6K
# Total Submissions: 2M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        # in the left branch, root is the new ceiling; contrarily root is the
        #  new floor in right branch
        return self.isValidBST(root.left, floor, root.val) and self.isValidBST(
            root.right, root.val, ceiling)


# @lc code=end
