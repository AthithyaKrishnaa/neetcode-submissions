class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}

        for str in strs:
            key="".join(sorted(str))

            if key not in hm:
                hm[key]=[]
            
            hm[key].append(str)
        
        return list(hm.values())