class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hm={}

        for num in numbers:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=1

        for i in range(len(numbers)):
            x=target-numbers[i]

            if x in numbers:
                return [i+1,numbers.index(x)+1]
        