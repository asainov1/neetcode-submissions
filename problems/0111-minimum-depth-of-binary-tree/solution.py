# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            # if root.val is not None:
            #     left_depth = self.minDepth(root.left)
            #     right_depth = self.minDepth(root.right)
            if not root.left:
                right_depth = self.minDepth(root.right)
                print (right_depth)
                return 1 + right_depth
            if not root.right:
                left_depth = self.minDepth(root.left)
                return 1 + left_depth
            # else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
