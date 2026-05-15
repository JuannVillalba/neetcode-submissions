class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}
        if len(s) != len(t): return False

        for i in range(len(s)):
          sMap[s[i]] = 1 + sMap.get(s[i] , 0)

        for i in range(len(t)):
          tMap[t[i]] = 1 + tMap.get(t[i] , 0)

        for i in range(len(s)):
          if s[i] in tMap:
            if sMap[s[i]] != tMap[s[i]]:
              return False
          else:
            return False

        return True 
