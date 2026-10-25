class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l, r = 0 , 0
        maxLength = 1
        mySet = set()

        while r < len(s):
            
            while  s[r] in mySet:
                mySet.remove(s[l])
                l += 1
                
            mySet.add(s[r])
            r += 1
            maxLength = max (maxLength , len(mySet))

        return maxLength
            
