class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       # stones = [-s for s in stones].   another way of doing it
        newStones = []
        for s in stones:
            newStones.append(-s)
        stones = newStones

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if y < x:
                heapq.heappush(stones, (y - x))
        
        if stones:
            return abs(stones[0])
        else: 
            return 0
        
