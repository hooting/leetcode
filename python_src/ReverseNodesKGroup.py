# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head
        fake = last = ListNode(0)
        fake.next = head
        while head:
            if not self.checkEnough(head,k): break
            first,tail = self.reverse(head,k)
            last.next = first
            last = tail
            head = last.next
        return fake.next

    def reverse(self,head,k):
        tail = head
        first = head
        second = first.next
        while k > 1:

            third = second.next
            second.next = first
            first = second
            second = third
            k -= 1
        tail.next = third
        return first,tail


    def checkEnough(self, head, k):
        while head and k > 0:
            k -= 1
            head = head.next
        if k == 0:
            return True
        else:
            return False