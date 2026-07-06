class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}

        for num in nums:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1
        
        res=sorted(hm.items(), key=lambda x:x[1], reverse=True)

        return [item[0] for item in res[:k]]