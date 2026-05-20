class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
             x = abs(heapq.heappop(stones))
             y = abs(heapq.heappop(stones))
             if x > y: x , y = y , x
             if x < y:
                heapq.heappush(stones, (y - x) * -1)      

        if stones:
            return abs(stones[0])
        else:
            return 0
