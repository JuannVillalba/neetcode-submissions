class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}  # num -> freq
        buckets = [[] for i in range(len(nums)) ]

        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        for n , f in freq.items():
            buckets[f - 1].append(n)

        res = []
        for i in range(len(buckets) -1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res



       



        



        
        
       