class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        row = len(mat)
        col = len(mat[0])
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = "#"        
        
        for i,j in queue:
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                r = i + di
                c = j + dj
                if 0 <= r < row and 0 <= c < col and mat[r][c] == "#":
                    mat[r][c] = mat[i][j] + 1
                    queue.append((r, c))
        return mat