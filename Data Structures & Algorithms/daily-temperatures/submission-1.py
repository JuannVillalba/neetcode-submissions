class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) 

        stack = [] # [temp , index]

        for i in range(len(temperatures)):
            temp = temperatures[i]

            while stack and temp > stack[-1][0]:
                stackT , stackI = stack.pop()
                res[stackI] = (i - stackI )
            stack.append([temp, i]) 
        
        return res