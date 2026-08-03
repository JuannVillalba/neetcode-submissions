class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) -1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target : return mid

            # we are on left
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
        
        return -1

        # 2 3 4 5 1

        # 4 6 7 0 1 2 3