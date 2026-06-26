class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        freq = defaultdict(int)
        l , r = 0 , 0
        for i in range(len(t)):
            freq[t[i]] += 1
        
        res , resL = [-1,-1] , float('infinity')
        have , need = 0 , len(freq)
        freq2 = defaultdict(int)
        for r in range(len(s)):
            freq2[s[r]] += 1
            if s[r] in freq and freq2[s[r]] == freq[s[r]]:
                have += 1


            while have == need:
                if (r-l + 1) < resL:
                    res = [l,r]
                    resL = (r-l+1)
                freq2[s[l]] -= 1
                if s[l] in freq and freq2[s[l]] < freq[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return s[l:r+1] if resL != float('infinity') else ""
        