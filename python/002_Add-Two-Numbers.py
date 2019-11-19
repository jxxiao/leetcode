# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = self.toint(l1) + self.toint(l2)


    def toint(self, node):
        return node.val + 10 * self.toint(node.next) if node else 0

