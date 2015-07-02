# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        fake = ListNode(0)
        fake.next = head
        pre = fake
        pivot = head
        while pivot != None:
            if pivot.val == val:
                pre.next = pivot.next
            else:
                pre = pivot
            pivot = pivot.next
        return fake.next