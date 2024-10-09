class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(remain, combine, start):
            if remain == 0:
                print(combine)
                res.append(list(combine))
                combine = []
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                combine.append(candidates[i])
                backtracking(remain - candidates[i], combine, i)
                combine.pop()
        
        combine = []
        backtracking(target, combine, 0)
        print(res)
        return res
