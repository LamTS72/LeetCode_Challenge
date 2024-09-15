class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        q = []
        row = len(mat)
        col = len(mat[0])
        for i in range(0, row):
            for j in range(0, col):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'

        for i, j in q:
            for dx, dy in (-1,0), (1, 0), (0, 1), (0, -1):
                nr = i + dx
                nc = j + dy
                if 0 <= nr < row and 0<= nc < col and mat[nr][nc] == '#':
                    mat[nr][nc] = mat[i][j] + 1
                    q.append((nr, nc))
        return mat
        
        