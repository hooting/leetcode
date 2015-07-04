# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        lh = rh = 0
        lPivot = rPivot = root
        while lPivot != None:
            lh += 1
            lPivot = lPivot.left
        while rPivot != None: 
            rh += 1
            rPivot = rPivot.right
        if lh == rh: return 2 ** lh - 1
        else: return 1 + self.countNodes(root.left) + self.countNodes(root.right)