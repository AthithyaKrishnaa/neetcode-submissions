class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}

        for word in strs:

            key="".join(sorted(word))

            if key not in hm:
                hm[key]=[]
            
            hm[key].append(word)

        return list(hm.values())