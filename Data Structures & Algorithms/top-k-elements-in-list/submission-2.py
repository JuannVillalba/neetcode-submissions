class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        res = []
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            freq[n] = 1 + freq.get(n, 0) 

        for n , f in freq.items():
            buckets[f].append(n)

        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]: 
                res.append(n)
                if len(res) == k:
                    return res 
        
       