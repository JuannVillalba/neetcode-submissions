class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        l, r = 0 , 1
        maxLength = 1
        mySet = set()

        if len(s) == 0:
            return 0
        while r < len(s):
            if len(mySet) < 1:
                mySet.add(s[l])
            while r < len(s) and s[r] not in mySet:
                mySet.add(s[r])
                r += 1
                maxLength = max (maxLength , len(mySet))
            while r < len(s) and s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            if r < len(s):
                mySet.add(s[r])
                r +=1
        return maxLength
            
