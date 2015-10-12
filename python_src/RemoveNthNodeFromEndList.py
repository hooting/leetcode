# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        second = head
        for i in range(n):
            second = second.next
        if second == None:
            return head.next
        first = head
        while second.next != None:
            first = first.next
            second = second.next
        first.next = first.next.next
        return head