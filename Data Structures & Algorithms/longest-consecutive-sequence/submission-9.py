class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        mySet = set(nums)

        for i in range(len(nums)):
            if (nums[i] -1) not in mySet:
                length = 1
                longest = max(length, longest)
                while (nums[i] + length) in mySet:
                    length += 1
                    longest = max(length,longest)                    
        return longest 