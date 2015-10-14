# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [(x.val,x) for x in lists if x]
        heapq.heapify(lists)
        head = pivot = ListNode(0)
        while lists:
            pivot.next = heapq.heappop(lists)[1]
            pivot = pivot.next
            if pivot.next != None:
                heapq.heappush(lists,(pivot.next.val,pivot.next))
        return head.next
        