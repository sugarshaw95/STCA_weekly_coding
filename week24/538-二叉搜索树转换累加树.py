# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        summ=0
        def helper(root):
            nonlocal summ

            if root:
                helper(root.right)
                summ+=root.val
                root.val=summ
                helper(root.left)
        helper(root)
        return root     
