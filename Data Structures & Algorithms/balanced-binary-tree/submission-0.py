# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(curr):
            if not curr:
                return 0
            
            right = dfs(curr.right)
            left = dfs(curr.left)
            if right == -1 or left == -1:
                return -1
            if right - left > 1 or right - left < -1:
                return -1
            else:
                return 1 + max(right,left)

        n = dfs(root)
        if n == -1:
            return False
        return True
        