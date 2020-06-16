# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        prev=None
        ret=None
        def inorder(n):
            nonlocal ret
            nonlocal prev
            if not n:
                return False
            if not inorder(n.left):

                #print(prev.val if prev else 'None',n.val)
                if prev:
                    if prev==p:
                        ret=n
                        prev=n
                        return True
            prev=n
            inorder(n.right)
        inorder(root)
        return ret
