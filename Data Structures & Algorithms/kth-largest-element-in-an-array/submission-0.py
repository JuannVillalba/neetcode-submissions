class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap of size K
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

        # add to heap, if 

        # len 5
        # k = 2