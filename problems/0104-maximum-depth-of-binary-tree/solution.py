# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        max_depth_l = self.maxDepth(root.left)
        max_depth_r = self.maxDepth(root.right)
        return 1 + max(max_depth_l, max_depth_r)
