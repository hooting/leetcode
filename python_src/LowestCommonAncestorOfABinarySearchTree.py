# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if (not p) or (not q) or (not root): return None
        pivot = root
        route = []
        while pivot.val != p.val:
            route.append(pivot)
            if pivot.val > p.val:
                pivot = pivot.left
            else:
                pivot = pivot.right
        route.append(pivot)
        parent = root
        pivot = root
        while pivot.val != q.val:
            if pivot.val > q.val:
                pivot = pivot.left
            else:
                pivot = pivot.right
            if len(route) == 1 or pivot.val != route[1].val:
                return route[0]
            else:
                del route[0]
        return route[0]
            