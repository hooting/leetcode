# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#The linked list can be divided into three parts, [0,m),[m,n],[n+1,length]
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        firstTail = head
        for i in range(m-2): firstTail = firstTail.next
        if m == 1:
            midHead = midPre = midTail = firstTail
        else:
            midHead = midPre = midTail = firstTail.next
        if not midHead: return head
        midTail = midTail.next
        #for loop, to make midPre point to the head of reversed second list, make midTail point to the head of third part
        for i in range(n - m):
            temp = midTail.next
            midTail.next = midPre
            midPre = midTail
            midTail = temp
        firstTail.next = midPre
        midHead.next = midTail
        if m == 1: return midPre
        return head
        
        