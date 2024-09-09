class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        b = []
        a = []
        p = 0
        n = len(grid) - 2
        for k in range(0,n*n):
            k = k%n
            for i in range(p,p+3):
                for j in range(k,k+3):
                    a.append(grid[i][j])
            if (k+1)%n == 0:
                p += 1    
            b.append(max(a))
            a = []
        for i in range(n):
            d = b[(i*n):(i*n+n)]
            res.append(d)


        return res