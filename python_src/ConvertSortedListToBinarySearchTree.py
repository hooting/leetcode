"""
reference to https://leetcode.com/discuss/10924/share-my-code-with-o-n-time-and-o-1-space
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        pivot = head
        num = 0
        self.head = head
        while pivot:
            num += 1
            pivot = pivot.next
        return self.buildTree(num)
    
    def buildTree(self, num):
        if num == 0: return None
        left = self.buildTree(num / 2)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.buildTree(num - num / 2 - 1)
        return root
        