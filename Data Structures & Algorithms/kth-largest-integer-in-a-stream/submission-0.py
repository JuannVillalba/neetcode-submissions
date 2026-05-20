class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth  = k
        self.nums = nums

    def add(self, val: int) -> int:
        
        self.nums.append(val)
        self.nums.sort()
        res = []
        for i in range(len(self.nums) -1 , -1, -1):
            res.append(self.nums[i])
            if len(res) == self.kth:
                return res[self.kth -1]

        
        # [1,2,3,3,3,5,6,7]