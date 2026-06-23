class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myMap = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            myMap[s[r]] = myMap.get(s[r], 0) + 1
            while (r-l + 1) - max(myMap.values()) > k:
                myMap[s[l]] -= 1
                l += 1 
            longest = max(longest , (r-l) +1)
        return longest