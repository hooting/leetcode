# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        ret = self.recursive(root,k)
        return ret[1]
    
    def recursive(self, root, k):
        if root == None:
            return (k,None)
        else:
            ret = self.recursive(root.left,k)
            k = ret[0]
            if k == 0:
                return ret
            elif k == 1:
                return (0,root.val)
            else:
                return self.recursive(root.right,k-1)
            