class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i != len(nums) -1:
            i += nums[i]
            if i > len(nums) -1:
                i = len(nums) -1
            if i != len(nums) -1:

                if nums[i] == 0:
                    return False
        return True 
