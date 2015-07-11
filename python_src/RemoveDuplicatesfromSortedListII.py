# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        fakeHead = ListNode(0)
        fakeHead.next = head
        leftNode = fakeHead
        preNode = pivotNode = head
        while preNode:
            try:
                if preNode.val == pivotNode.val:
                    pivotNode = pivotNode.next
                else:
                    if preNode.next == pivotNode:
                        leftNode.next = preNode
                        leftNode = preNode
                    else:
                        preNode = pivotNode
            except AttributeError:
                if preNode == None or preNode.next == None:
                    leftNode.next = preNode
                else:
                    leftNode.next = None
                break
        return fakeHead.next