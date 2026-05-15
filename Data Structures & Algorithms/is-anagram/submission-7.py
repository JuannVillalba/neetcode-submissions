class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sFreq = [0] * 26 
        tFreq = [0] * 26 
        if len(s) != len(t): return False

        for i in range(len(s)):
          sFreq[ord('z') - ord(s[i])] +=1
          tFreq[ord('z') - ord(t[i])] +=1

        for i in range(len(sFreq)):
          if sFreq[i] != tFreq[i]:
            return False
        
        return True


        
