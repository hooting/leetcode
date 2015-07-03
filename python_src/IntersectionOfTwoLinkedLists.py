# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        pivot = headA
        lenA = lenB = 0
        while pivot != None:
            lenA += 1
            pivot = pivot.next
        pivot = headB
        while pivot != None:
            lenB += 1
            pivot = pivot.next
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB,lenA
        step = 0
        pivotA = headA
        pivotB = headB
        while step < lenA - lenB:
            pivotA = pivotA.next
            step += 1
        while pivotA != None and pivotB != None:
            if pivotA == pivotB: return pivotA
            else:
                pivotA = pivotA.next
                pivotB = pivotB.next
        return None