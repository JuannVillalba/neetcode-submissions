class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for i in range(len(nums)):
            length = 0
            if (nums[i] -1) not in mySet:
                length += 1
                while (nums[i] +length) in mySet:
                    length +=1
                if length > longest:
                    longest = length
            
        return longest
                                




       
                    

                

