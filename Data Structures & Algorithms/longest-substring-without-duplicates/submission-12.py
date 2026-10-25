class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l , r = 0, 0
        longest = 0
        mySet = set()
        for i in range(len(s)):
            
            if s[i] not in mySet:
                mySet.add(s[i])
                longest = max (longest, ((r-l) +1))
                r += 1
            else:
                l +=1
                while l < r and s[l] == s[l-1]:
                    l += 1 

        return longest
