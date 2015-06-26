# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        pivot = head
        while pivot != None and pivot.next != None:
            if pivot.val == pivot.next.val:
                pivot.next = pivot.next.next
            else:
                pivot = pivot.next
        return head