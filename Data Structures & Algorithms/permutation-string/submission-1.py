class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26
        if len(s2) < len(s1): return False
        for i in range(len(s1)):
            freq[ord(s1[i]) - ord('a')] += 1
        
        l , r = 0,0
        for i in range(len(s1)):
            r += 1
        
        while r <= len(s2):
            freq2 = [0] * 26
            for i in range(len(s1)):
                freq2[ord(s2[i + l]) - ord('a')] += 1
            if freq == freq2: return True
            l += 1
            r += 1
        
        return False