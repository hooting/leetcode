# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        pivot = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                pivot.next = l1
                l1 = l1.next
            else:
                pivot.next = l2
                l2 = l2.next
            pivot = pivot.next
        if l1 == None:
            l1 = l2
        pivot.next = l1
        return head.next
                
        