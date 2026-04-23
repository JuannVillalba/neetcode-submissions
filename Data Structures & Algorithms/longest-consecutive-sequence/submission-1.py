class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        mySet = set(nums)
        
        for n in nums:
            if (n - 1) not in mySet:
                length = 0
                
                while (n + length) in mySet:
                    length += 1 

                if length > longest:
                    longest = length
        
        return longest
                    

                

