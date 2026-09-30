class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mySet = set()

        for i in range(len(nums)):
            print("one")
            if nums[i] in mySet:
                return True
            else:
                mySet.add(nums[i])

        return False