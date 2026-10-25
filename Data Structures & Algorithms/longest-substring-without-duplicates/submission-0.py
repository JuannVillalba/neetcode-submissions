class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 1
        maxLength = 1

        while r < len(s):
            
            mySet = set()
            mySet.add(s[l])
            while s[r] not in mySet:
                mySet.add(s[r])
                r += 1
                maxLength = max (maxLength , len(mySet))
            
            l = r
            r += 1
        
        return maxLength
            
