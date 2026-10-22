class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l , r = 0 , 0
        longest = 0
        while r < len(s):
            if s[r] not in mySet:
                mySet.add(s[r])
            else:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    l += 1
                mySet.add(s[r])    
            longest = max(longest, (r-l) +1 )
            r +=1 
        return longest   
