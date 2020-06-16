# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        res=[]
        minn=float('inf')
        prev=-float('inf')
        def inorder(root):

            if not root:
                return
            nonlocal minn
            nonlocal prev
            if root.left:
                inorder(root.left)
            cur=root.val
            if cur-prev<minn:
                minn=cur-prev
            prev=cur
            #res.append(root.val)
            #print(res)
            if root.right:
                inorder(root.right)
        inorder(root)
        #print(res)

        return minn
