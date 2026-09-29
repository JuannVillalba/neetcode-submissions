class Solution:
    def trap(self, height: List[int]) -> int:

        totalWater = 0
        l, r = 0 , len(height) -1

        maxLeft = height[l]
        maxRight = height[r]

      #  min (height[l], height[r])

        while l < r:

            if maxLeft < maxRight:
                l += 1
                if maxLeft < height[l]:
                    maxLeft = height[l]
                totalWater += maxLeft - height[l]
            else:
                r -= 1
                if maxRight < height[r]:
                    maxRight = height[r]
                totalWater += maxRight - height[r]
        
        return totalWater



            

    