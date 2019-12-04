'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-12-02 15:45:57
@LastEditors: jxxiao
@LastEditTime: 2019-12-03 18:18:27
'''
#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (36.05%)
# Likes:    1050
# Dislikes: 57
# Total Accepted:    135.8K
# Total Submissions: 372K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
#
# Input: [1,3,null,null,2]
#
# 1
# /
# 3
# \
# 2
#
# Output: [3,1,null,null,2]
#
# 3
# /
# 1
# \
# 2
#
#
# Example 2:
#
#
# Input: [3,1,4,null,null,2]
#
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
#
# Output: [2,1,4,null,null,3]
#
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
#
#
# Follow up:
#
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
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
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node):
            if node.left:
                yield from inorder(node.left)
            yield node
            if node.right:
                yield from inorder(node.right)
        # Tree.drawtree(Tree.deserialize(root))

        swap1 = swap2 = smaller = None
        for node in inorder(root):
            if smaller and smaller.val > node.val:
                if not swap1:
                    swap1 = smaller
                swap2 = node
            smaller = node
        if swap1:
            swap1.val, swap2.val = swap2.val, swap1.val


# @lc code=end
