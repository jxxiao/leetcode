'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-04-19 17:36:46
@LastEditors: jxxiao
@LastEditTime: 2020-04-19 17:42:12
'''
#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (65.07%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    17.8K
# Total Submissions: 27.4K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其层序遍历:
#
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
#
#
#
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
#
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            path = []
            new_queue = []
            for node in queue:
                path.append(node.val)
                new_queue.extend(node.children)
            queue = new_queue
            res.append(path)
        return res

# @lc code=end
