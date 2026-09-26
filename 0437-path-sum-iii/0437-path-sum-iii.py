# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, cursum):
        if not node:
            return 0
        count = 0
        cursum += node.val
        if cursum == self.targetSum:
            count += 1

        count += self.dfs(node.right, cursum)
        count += self.dfs(node.left, cursum)
        return count
    def visit(self, node):
        if not node:
            return 0
        return (self.dfs(node, 0) + self.visit(node.left) + self.visit(node.right) )
    
    
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        """
        Binary tree
        in balanced: TC: O(log n) SC: O(log n)
        in unbalanced: TC: O(n) SC: O(n)
        DFS TC: O(v) SC: O(v - 1). не корневые узлы 

        """
        self.targetSum = targetSum
        self.cur_sum = 0
        return self.visit(root)