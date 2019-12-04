'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-04 11:58:19
@LastEditors: jxxiao
@LastEditTime: 2019-12-04 12:04:17
'''
#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (53.22%)
# Likes:    1591
# Dislikes: 161
# Total Accepted:    320.7K
# Total Submissions: 595.9K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.dfs(nums, 0, len(nums)-1)

    def dfs(self, nums, l, r):
        if l <= r:
            mid = (r+l)//2
            root = TreeNode(nums[mid])
            root.left = self.dfs(nums, l, mid - 1)
            root.right = self.dfs(nums, mid + 1, r)
            return root

# @lc code=end
