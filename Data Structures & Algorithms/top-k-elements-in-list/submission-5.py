class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # num -> freq

        #populate map, loop
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i] , 0)

        # populate heapwith frq and num
        heap = []
        for n in freq.keys():
            heapq.heappush(heap , (freq[n], n))
            while len(heap) > k:
                heapq.heappop(heap)

        #populate array w K most frequent nums
        res =[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1] )

        #return arr
        return res


       



        



        
        
       