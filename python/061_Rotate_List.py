# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        pointer = head
        length = 1

        while pointer.next:
            length += 1
            pointer = pointer.next

        rotateTimes = k % length
        if rotateTimes == 0:
            return head
        fastPointer = slowPointer = head
        for _ in range(rotateTimes):
            fastPointer = fastPointer.next

        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        slowPointer.next, fastPointer.next, head = None, head, slowPointer.next

        return head


