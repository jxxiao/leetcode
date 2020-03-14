'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-01-06 21:23:47
@LastEditors: jxxiao
@LastEditTime: 2020-02-19 01:08:19
'''
#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (39.91%)
# Likes:    1406
# Dislikes: 130
# Total Accepted:    297.1K
# Total Submissions: 724.5K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
#
#
#
# Example 1:
#
#
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer to point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000
#
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root or (root.left is None and root.right is None):
            return root
        if root.left and root.right:
            root.left.next = root.right
            root.right.next = self.getNextNotNullChild(root)
        if root.left is None:
            root.right.next = self.getNextNotNullChild(root)
        if root.right is None:
            root.left.next = self.getNextNotNullChild(root)
        root.right = self.connect(root.right)
        root.left = self.connect(root.left)
        return root

    def getNextNotNullChild(self, root):
        while root.next:
            if root.next.left:
                return root.next.left
            if root.next.right:
                return root.next.right
            root = root.next
        return None



# @lc code=end
