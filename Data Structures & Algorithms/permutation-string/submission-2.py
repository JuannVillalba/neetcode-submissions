class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        if len(s2) < len(s1): return False
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
        
        l , r = 0 , 0
        freq2 = [0] * 26
        while r < len(s2):
            freq2[ord(s2[r]) - ord('a')] += 1
            if r > len(s1) - 1:
                freq2[ord(s2[l]) - ord('a')] -= 1
                l += 1 
            if freq == freq2: return True
            r += 1
        return False