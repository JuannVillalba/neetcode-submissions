class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       sString = {}
       tString = {}

       for c in s:
         sString[c] = sString.get(c, 0) + 1

       for ct in t:
         tString[ct] = tString.get(ct, 0) + 1

       if sString == tString:
         return True
       else:
        return False
