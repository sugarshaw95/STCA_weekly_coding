# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def height(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return max(height(root.left),height(root.right))+1
        h1=height(root.left)
        h2=height(root.right)
        return abs(h1-h2)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
