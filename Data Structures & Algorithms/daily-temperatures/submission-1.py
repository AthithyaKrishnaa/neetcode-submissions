class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        results=[0]*len(temperatures)

        for i,val in enumerate(temperatures):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                results[prev]=i-prev
            stack.append(i)
        return results
