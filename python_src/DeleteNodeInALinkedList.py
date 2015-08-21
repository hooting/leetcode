# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node or not node.next: return
        post = node.next
        while post.next:
            node.val = post.val
            node = post
            post = post.next
        node.val = post.val
        node.next = None
        