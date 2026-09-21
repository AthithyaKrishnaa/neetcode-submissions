class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for st in strs:
            key="".join(sorted(st))
            if key not in hm:
                hm[key]=[]
            hm[key].append(st)
        
        return list(hm.values())  
