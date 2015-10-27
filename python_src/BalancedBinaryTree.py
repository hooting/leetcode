# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a,b = self.checkBalance(root)
        return b
        
    def checkBalance(self, root):
        if root == None: return 0,True
        leftH, leftB = self.checkBalance(root.left)
        rightH, rightB = self.checkBalance(root.right)
        if abs(leftH - rightH) <= 1 and leftB and rightB:
            return max(leftH, rightH) + 1, True
        else:
            return 0, False
        