# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        pivot = root
        while pivot or len(stack) > 0:
            while pivot:
                stack.append(pivot)
                pivot = pivot.left
            pivot = stack[-1]
            del stack[-1]
            result.append(pivot.val)
            pivot = pivot.right
        return result