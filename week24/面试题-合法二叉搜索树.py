# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        if not root:
            return True
        if root.left:
            if root.left.val>=root.val:
                return False
            if not self.isValidBST(root.left):
                return False
        if root.right:
            if root.right.val<=root.val:
                return False
            if not self.isValidBST(root.right):
                return False        
        return True
        '''
        prev=-float('inf')
        #cur=
        yes=True
        def inorder(root):
            nonlocal prev
            nonlocal yes
            if not root:
                return
            inorder(root.left)
            if prev>=root.val:
                yes=False
                return
            prev=root.val
            inorder(root.right)
        inorder(root)
        return yes
