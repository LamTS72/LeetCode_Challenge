class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        print(res)
        stack = [0]
        for i in range(1, len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                day = i - idx
                res[idx] = day
            stack.append(i)
        
        print(res)
        return res
