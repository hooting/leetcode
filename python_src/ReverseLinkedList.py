# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None: return head
        pre = head
        pivot = head.next
        pre.next = None
        while pivot != None:
            next = pivot.next
            pivot.next = pre
            pre = pivot
            pivot = next
        return pre