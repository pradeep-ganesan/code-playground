# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p and not q) or (q and not p):
            return False
        if p:
            if p.val != q.val:
                return False
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            if not left or not right:
                return False
        return True
