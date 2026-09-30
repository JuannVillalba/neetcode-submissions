class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        aMap = defaultdict(list)
        for s in strs:
            array = [0] * 26
            for c in s:
                code = ord(c) - ord('a')  
                array[code] +=1 
            
            aMap[tuple(array)].append(s)
        
        return list(aMap.values())




        