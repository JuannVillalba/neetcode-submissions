# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return 0
        count += 1
        queue = deque([root])
        countLeft = 1
        countRight = 1

        while queue:
            node = queue.popleft()
            if node.left:
                countLeft += 1
                queue.append(node.left)
            if node.right:
                countRight += 1
                queue.append(node.right)

        count = max(countLeft, countRight)
        return count
