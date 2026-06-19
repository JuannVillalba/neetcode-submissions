class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # key->freq val->strs[i]
        for i in range (len(strs)):
            freq = [0] * 26
            for l in (strs[i]):
                freq[ord(l) - ord('a')] += 1
            res[tuple(freq)].append(strs[i])
        return list(res.values())

           
        



        
