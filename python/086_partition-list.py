#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (38.75%)
# Likes:    859
# Dislikes: 228
# Total Accepted:    182.9K
# Total Submissions: 471.5K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_left = small_right = ListNode(0)
        big_left = big_right = ListNode(0)
        while head:
            if head.val < x:
                small_right.next = head
                small_right = small_right.next
            else:
                big_right.next = head
                big_right = big_right.next
            head = head.next
        small_right.next = big_left.next
        big_right.next = None
        return small_left.next


# @lc code=end
