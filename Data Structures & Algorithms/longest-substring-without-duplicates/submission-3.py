class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 1
        maxLength = 1
        mySet = set()
        while r < len(s):
            
            if len(mySet) < 1:
                mySet.add(s[l])
            
            while r < len(s) and s[r] not in mySet:
                mySet.add(s[r])
                r += 1
                maxLength = max (maxLength , len(mySet))
            
            if s[r] in mySet and r < len(s):
                mySet.remove(s[l])
                mySet.add(s[r])
                l += 1
                r += 1
                
            
           
        
        return maxLength
            
