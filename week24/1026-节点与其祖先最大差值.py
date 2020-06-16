# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        minn=root.val
        maxx=root.val
        ret=0
        def preorder(root,maxx,minn):
            if not root:
                return
            #nonlocal minn
            nonlocal ret
            #nonlocal maxx
            #print(minn,maxx,root.val)
            if (root.val-minn)>ret:
                ret=(root.val-minn)
            if maxx-root.val>ret:
                ret=maxx-root.val

            if root.val<minn:
                minn=root.val
            if root.val>maxx:
                maxx=root.val
            preorder(root.left,maxx,minn)
            preorder(root.right,maxx,minn)
        preorder(root,maxx,minn)
        return ret
