# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None
        result = []
        for list in lists:
            while(list):
                result = result.append(list.val)
                list = list.next
        result.sort()

        head = dumphead = ListNode(None)

        for x in result:
            head.next = ListNode(x)
            head = head.next
        return dumphead.next

