class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x=target-numbers[i]

            if x in numbers:
                return [i+1,numbers.index(x)+1]
        