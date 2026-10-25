class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l , r = 0 , (rows * cols) -1

        while l <= r:
            mid = l + r-l //2
            row , col = mid // cols , mid % cols
            if mid == target: return True
            elif mid < target:
                l = mid + 1
            else:
                r = mid - 1
        return False