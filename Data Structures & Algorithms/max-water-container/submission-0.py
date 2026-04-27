class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mostArea = 0
        
        for i in range(len(heights)):
            l , r = i , len(heights) -1

            while l < r:
                height = min(heights[l], heights[r])
                thisArea = height * (r - (l))

                if thisArea > mostArea:
                    mostArea = thisArea

                r -=1
            

        return mostArea

       
