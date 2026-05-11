class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l, r = 0 , 0
        maxLength = 0
        mySet = set()

        while r < len(s):
            while  s[r] in mySet:
                mySet.remove(s[l])
                l += 1

            mySet.add(s[r])
            maxLength = max (maxLength , len(mySet))
            r += 1

        return maxLength
            
