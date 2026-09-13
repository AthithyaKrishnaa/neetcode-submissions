class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}
        for s in strs:
            key="".join(sorted(s))
            if key not in hm:
                hm[key]=[]
            hm[key].append(s)
        return list(hm.values())