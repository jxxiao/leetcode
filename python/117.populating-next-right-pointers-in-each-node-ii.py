#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (35.92%)
# Likes:    1257
# Dislikes: 167
# Total Accepted:    223.9K
# Total Submissions: 604.9K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
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
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100
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
    def connect(self, root):
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
