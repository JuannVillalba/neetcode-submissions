class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l , r = 0, 0
        longest = 0
        mySet = set()
        for i in range(len(s)):
            
            if s[i] not in mySet:
                mySet.add(s[i])
                longest = max (longest, len(mySet))
            else:
                mySet = set()
                mySet.add(s[i])

        
        return longest
