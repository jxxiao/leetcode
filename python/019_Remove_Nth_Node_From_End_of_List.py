# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current, temp = head, head

        for i in range(n):
            temp = temp.next

        if not temp:
            return head.next
        while temp.next is not None:
            temp = temp.next
            current = current.next

        current.next = current.next.next
        return head

    def removeNthFromEnd_two(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        def retreat(runner):
            if (runner is not None): return 0
            i = retreat(runner.next)
            if i == n:
                runner.next == runner.next.next
            return i + 1

        retreat(dummy)
        return dummy.next
