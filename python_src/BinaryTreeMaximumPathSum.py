# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxium = -0x7fffffff
        self.maxSubPath(root)
        return self.maxium
    
    def maxSubPath(self, root):
        if not root: return 0
        left = self.maxSubPath(root.left)
        right = self.maxSubPath(root.right)
        if left > 0 and right > 0:
            self.maxium = max(self.maxium, left + right + root.val)
            return root.val + max(left,right)
        else:
            max_sub = max(root.val, max(right,left) + root.val) #if right and left both are < 0, the max sub path is root
            self.maxium = max(self.maxium, max_sub)
            return max_sub
            