class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {} # val -> index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in myMap: return [myMap[diff], i]
            myMap[nums[i]] = i
            
