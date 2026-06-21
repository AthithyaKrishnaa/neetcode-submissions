class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}

        for num in nums:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1
        
        res=sorted(hm,key=hm.get,reverse=True)

        return res[:k]
