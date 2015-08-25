# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        ret = self.getUtil(root)
        ret = map(lambda x: "->".join(x[::-1]),ret)
        return ret
    
    def getUtil(self,root):
        if root.left == root.right == None:
            return [[str(root.val)]]
        ret = []
        if root.left:
            ret = self.mergeUtil(root.val,root.left)
        if root.right:
            ret += self.mergeUtil(root.val,root.right)
        return ret
            
    def mergeUtil(self,val,root):
        ret = self.getUtil(root)
        map(lambda x: x.append(str(val)), ret)
        return ret
        