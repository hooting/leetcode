# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = pivot = ListNode(0)
        carry_bit = 0
        l1_pivot = l1
        l2_pivot = l2
        while l1_pivot and l2_pivot:
            carry_bit, mod = divmod(carry_bit + l1_pivot.val + l2_pivot.val,10)
            pivot.next = ListNode(mod)
            pivot = pivot.next
            l1_pivot = l1_pivot.next
            l2_pivot = l2_pivot.next
            
        if l2_pivot: l1_pivot = l2_pivot
        while l1_pivot:
            carry_bit, mod = divmod(carry_bit + l1_pivot.val,10)
            pivot.next = ListNode(mod)
            pivot = pivot.next
            l1_pivot = l1_pivot.next
        if carry_bit != 0:
            pivot.next = ListNode(carry_bit)
        return head.next