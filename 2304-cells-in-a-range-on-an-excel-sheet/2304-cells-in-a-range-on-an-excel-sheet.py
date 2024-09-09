class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        min_row = int(s[1])
        max_row = int(s[-1])
        max_col = int(ord(s[-2]) - ord(s[0]) + 1)
        min_col = s[0]
        for j in range(max_col):
            for i in range(min_row,max_row+1):
                string = str(chr(ord(min_col) + j)) + str(i)
                res.append(string)
        print(res)
        return res

        