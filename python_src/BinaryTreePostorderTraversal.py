# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        pivot = root
        stack = []
        while pivot or len(stack) > 0:
            while pivot:
                stack.append((0,pivot))
                pivot = pivot.left
            pivot = stack[-1]
            if pivot[0] == 1: 
                while len(stack) > 0 and pivot[0] == 1:
                    pivot = stack[-1]
                    result.append(pivot[1].val)
                    del stack[-1]
                if pivot[0] == 0: 
                    del result[-1]
                    stack.append((1,pivot[1]))
                else: break
            else:
                stack[-1] = (1,pivot[1])
            pivot = pivot[1].right
        return result