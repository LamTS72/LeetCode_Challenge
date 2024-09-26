class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        count_c = 0
        count_r = 0
        res = []
        for row in range(0, n-2):
            compute = []
            for col in range(0, n-2):
                matrix = []
                for sub_r in range(0, 3):
                    for sub_c in range(0, 3):
                        matrix.append(grid[row+sub_r][col+sub_c])
                compute.append(max(matrix))
            res.append(compute)
        print(res)
        return res
