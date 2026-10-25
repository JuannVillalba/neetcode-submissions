class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i+1 , len(nums) -1

            if nums[i] > 0:
                break
            
            if nums[i] == nums[i-1]:
                continue
            
            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if threesum > 0:
                    r -=1
                elif threesum < 0:
                    l +=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        
        return res

        
       # [-4,-1,-1,0,1,2]