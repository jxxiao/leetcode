'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-03 23:42:32
@LastEditors: jxxiao
@LastEditTime: 2019-12-03 23:45:24
'''
#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (43.68%)
# Likes:    1360
# Dislikes: 76
# Total Accepted:    278.2K
# Total Submissions: 629K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, root, level, res):
        if not root:
            return
        if len(res) < level + 1:
            res.append([])
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        self.dfs(root.left, level + 1, res)
        self.dfs(root.right, level + 1, res)


# @lc code=end
