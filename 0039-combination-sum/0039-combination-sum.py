class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combine = []
        start = 0
        def backtracking(remain, combine, start):
            if remain == 0:
                res.append(list(combine))
                combine = []
                return 
            elif remain < 0:
                return
            
            for i in range(start, len(candidates)):
                combine.append(candidates[i])
                backtracking(remain - candidates[i], combine, i)
                combine.pop()


        backtracking(remain=target, combine=combine, start=start)
        return res


        
