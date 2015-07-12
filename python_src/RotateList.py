# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        count = 1
        pre = head
        pivot = head.next
        head.next = None
        while pivot != None:
            temp = pivot.next
            pivot.next = pre
            pre = pivot
            pivot = temp
            count += 1
        k %= count
        #after the pre while loop, 
        #pre points to the head of linked list
        #head points to the tail of linked list
        while k > 0:
            head.next = pre
            pre = pre.next
            head = head.next
            head.next = None
            k -= 1
        #the pre while loop does move k elements to the tail of linked list
        pivot = pre.next
        pre.next = None
        while pivot != None:
            temp = pivot.next
            pivot.next = pre
            pre = pivot
            pivot = temp
        return pre
        
        