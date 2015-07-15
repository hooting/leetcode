# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if (not head) or (not head.next): return True
        step1 = step2 = head
        while step2 and step2.next:
            step2 = step2.next.next
            step1 = step1.next
        pre = head
        pivot = head.next
        pre.next = None
        while pivot != step1:
            temp = pivot.next
            pivot.next = pre
            pre = pivot
            pivot = temp
        if step2: pivot = step1.next
        else: pivot = step1
        while pre:
            if pre.val != pivot.val: return False
            pre = pre.next
            pivot = pivot.next
        return True
        