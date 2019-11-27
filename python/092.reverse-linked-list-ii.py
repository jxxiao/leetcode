'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-27 11:11:23
@LastEditors: jxxiao
@LastEditTime: 2019-11-27 16:51:39
'''
#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (36.34%)
# Likes:    1586
# Dislikes: 109
# Total Accepted:    225.8K
# Total Submissions: 617.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):
            pre = pre.next
        cur = pre.next
        # reverse the defined party
        node = None
        for _ in range(n - m + 1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        # connect three parts
        pre.next.next = cur
        pre.next = node
        return dummy.next


# @lc code=end
