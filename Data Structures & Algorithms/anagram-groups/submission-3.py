class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm={}

        for strr in strs:
            word="".join(sorted(strr))

            if word not in hm:
                hm[word]=[]
            
            hm[word].append(strr)

        return list(hm.values())