class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def dfs(sr, sc):
            if sr not in range(len(image)): return
            if sc not in range(len(image[0])): return
            if image[sr][sc] == red_color: return
            if image[sr][sc] != blue_color: return

            image[sr][sc] = red_color
            dfs(sr-1, sc)
            dfs(sr+1, sc)
            dfs(sr, sc-1)
            dfs(sr, sc+1)
        
        blue_color = image[sr][sc]
        red_color = color
        dfs(sr, sc)
        return image