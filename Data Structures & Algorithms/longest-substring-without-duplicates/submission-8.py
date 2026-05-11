class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l , r = 0 , 0
        mySet = set()
        longest = 0

        while r < len(s):
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[r])
            longest = max(longest , len(mySet))
            r +=1
        return longest
     
            
